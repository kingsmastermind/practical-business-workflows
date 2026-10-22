from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,subprocess,math
R=Path(__file__).resolve().parent; C=R/'captures';O=R/'videos';O.mkdir(exist_ok=True)
routes=json.loads((C/'routes.json').read_text());fixtures=json.loads((R/'fixtures.json').read_text());font='/System/Library/Fonts/Supplemental/Arial.ttf';bold='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
W,H,FPS=1600,1080,12
for key,states in routes.items():
 imgs=[Image.open(C/f'{key}-{i}.png').convert('RGB') for i in range(4)];p=fixtures[key];sw,sh=imgs[0].size;scale=min(1520/sw,900/sh);nw,nh=int(sw*scale),int(sh*scale);ox,oy=(W-nw)//2,65
 scaled=[im.resize((nw,nh)) for im in imgs];proc=subprocess.Popen(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-an','-c:v','libx264','-preset','ultrafast','-crf','22','-pix_fmt','yuv420p','-movflags','+faststart',str(O/f'{key}.mp4')],stdin=subprocess.PIPE)
 for f in range(24*FPS):
  t=f/FPS;i=min(3,int(t//6));u=(t%6)/6;im=Image.new('RGB',(W,H),'#101217');im.paste(scaled[max(0,i-1) if i>0 and u<.20 else i],(ox,oy));d=ImageDraw.Draw(im);d.text((45,22),p['name'],font=ImageFont.truetype(bold,22),fill='#f2f0e8');d.text((1180,25),'SYNTHETIC DEMO / NO AUDIO',font=ImageFont.truetype(font,15),fill='#b5becd')
  target=states[i]['rect'];tx=ox+(target['x']+target['width']*.65)*scale;ty=oy+(target['y']+target['height']*.5)*scale
  old=states[max(0,i-1)]['rect'];sx=ox+(old['x']+old['width']*.65)*scale;sy=oy+(old['y']+old['height']*.5)*scale;e=min(1,u*8);e=e*e*(3-2*e);x=sx+(tx-sx)*e;y=sy+(ty-sy)*e
  # Cursor demonstrates the captured tab navigation; no slow camera zoom.
  d.polygon([(x,y),(x+2,y+29),(x+10,y+21),(x+18,y+36),(x+25,y+32),(x+16,y+18),(x+28,y+17)],fill='white',outline='#171717',width=2)
  if .1<u<.28:
   radius=int(8+35*(u-.1)/.18);d.ellipse((tx-radius,ty-radius,tx+radius,ty+radius),outline='#e9bd46',width=3)
  if .30<u<.88:
   r=states[i]['focus'];a=ox+r['x']*scale;b=oy+r['y']*scale;ww=min(r['width']*scale,nw-220);hh=min(r['height']*scale,330);d.rounded_rectangle((a-4,b-4,a+ww+4,b+hh+4),radius=9,outline='#e9bd46',width=3)
  cap=p['captions'][i];d.rounded_rectangle((40,975,1560,1050),radius=10,fill='#252a33');ff=ImageFont.truetype(bold,23)
  if d.textlength(cap,font=ff)>1460:ff=ImageFont.truetype(bold,20)
  d.text((66,1000),f'{i+1:02d} / {cap}',font=ff,fill='#f8f7f1');d.rectangle((40,1069,1560,1073),fill='#333943');d.rectangle((40,1069,40+int(1520*t/24),1073),fill='#e9bd46');proc.stdin.write(im.tobytes())
 proc.stdin.close();assert proc.wait()==0;print(key+' rendered',flush=True)
 # Standalone captions, also used by the synchronized below-player guide.
 v='WEBVTT\n\n'
 for i,c in enumerate(p['captions']):v+=f'{i+1}\n00:{i*6:02d}.000 --> 00:{(i+1)*6:02d}.000\n{c}\n\n'
 (O/f'{key}.vtt').write_text(v)
# A short montage uses excerpts, not seven complete walkthroughs.
for key in routes:
 subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss','6','-i',str(O/f'{key}.mp4'),'-t','3','-an','-c:v','libx264','-preset','ultrafast','-crf','22',str(O/f'{key}-excerpt.mp4')],check=True)
(O/'montage-list.txt').write_text(''.join("file '"+key+"-excerpt.mp4'\n" for key in routes))
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',str(O/'montage-list.txt'),'-c','copy','-movflags','+faststart',str(O/'montage.mp4')],check=True)
print('Montage rendered',flush=True)
