export class IntakeQueue {
  #seen = new Map();
  events = [];
  accept(input) {
    if (!input || typeof input.eventId !== 'string' || !input.eventId.trim()) throw new Error('Event ID required');
    if (this.#seen.has(input.eventId)) return { ...this.#seen.get(input.eventId), duplicate: true };
    if (typeof input.email !== 'string' || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.email)) throw new Error('Valid email required');
    const team = input.kind === 'service' ? 'operations' : 'sales';
    const record = { eventId: input.eventId, email: input.email.trim().toLowerCase(), team, status: 'review', followUpAllowed: input.optedIn === true };
    this.#seen.set(input.eventId, record);
    this.events.push({ eventId: record.eventId, action: 'accepted', team });
    return { ...record };
  }
  transition(eventId, signal) {
    const record = this.#seen.get(eventId);
    if (!record) throw new Error('Unknown event');
    if (!['reply', 'human', 'optout', 'booked'].includes(signal)) throw new Error('Unknown signal');
    record.followUpAllowed = false;
    record.status = { reply: 'needs_reply', human: 'human_review', optout: 'suppressed', booked: 'scheduled' }[signal];
    this.events.push({ eventId, action: signal, status: record.status });
    return { ...record };
  }
}
