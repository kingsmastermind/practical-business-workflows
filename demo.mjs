import { IntakeQueue } from './workflow.mjs';
const q = new IntakeQueue();
console.log(q.accept({eventId:'demo-001',email:'alex@example.test',kind:'service',optedIn:true}));
console.log(q.transition('demo-001','human'));
console.log(q.events);
