from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import subprocess,math,json,os
ROOT=Path(__file__).parent; ASSETS=Path(os.environ['SHOWCASE_ASSET_DIR']); M=ROOT/'media'
scenes=[('Customer communications','From request to a useful reply.','A service request stays alongside the customer message and a prepared response.','m41lb0x-synthetic-onboarding-v1-screen.png','Keep the conversation and next action together.'),('Sales preparation','Context before the conversation.','Discovery questions turn a research brief into a focused conversation plan.','precall-synthetic-v1-screen.png','Ask questions tied to the buyer\'s stated pain.'),('Operational visibility','See the work across the business.','A shared control surface brings operational status and attention into one view.','x4vier-control-plane-v1-screen.png','Give the operator a clear view of what needs attention.'),('Research workspace','Make information navigable.','Organized evidence gives research a place to be reviewed and used.','private-intel-synthetic-v1-screen.png','Keep the useful evidence close to the decision.')]
font='/System/Library/Fonts/Supplemental/Arial.ttf';bold='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
def ft(n,b=False):return ImageFont.truetype(bold if b else font,n)
def wrap(d,text,x,y,width,f,color,spacing=10):
 words=text.split();line=''
 for w in words:
  if d.textlength(line+' '+w,font=f)>width and line:d.text((x,y),line,font=f,fill=color);y+=f.size+spacing;line=w
  else:line=(line+' '+w).strip()
 d.text((x,y),line,font=f,fill=color);return y+f.size+spacing
W,H=1600,900;fps=15;duration=48
proc=subprocess.Popen(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-vcodec','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(fps),'-i','-','-an','-c:v','libx264','-preset','fast','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart',str(M/'guided-product-walkthrough.mp4')],stdin=subprocess.PIPE)
imgs=[Image.open(ASSETS/s[3]).convert('RGB') for s in scenes]
for frame in range(fps*duration):
 t=frame/fps;i=min(3,int(t//12));u=(t%12)/12;s=scenes[i];im=Image.new('RGB',(W,H),'#090d12');d=ImageDraw.Draw(im)
 d.text((70,44),'ROBB TENEO / SYSTEMS IN PRACTICE',font=ft(22,True),fill='#f5f4ef');d.text((1150,48),'SYNTHETIC PRODUCT DATA',font=ft(16),fill='#d8b771');d.line((70,100,1530,100),fill='#3e372b',width=1)
 # Calm entrance; shot holds long enough to read.
 offset=int(24*(1-min(1,u*7))**2);d.text((70,200+offset),f'0{i+1} / {s[0].upper()}',font=ft(20,True),fill='#d8b771');y=wrap(d,s[1],70,250+offset,540,ft(51,True),'#faf8f3',12);wrap(d,s[2],70,y+25,510,ft(27),'#b7bec7',13)
 # Animate camera framing, not imaginary UI actions.
 box=(680,155,1530,710);src=imgs[i];bw,bh=box[2]-box[0],box[3]-box[1]
 if src.height>src.width*1.5:
  scale=bw/src.width;new=src.resize((bw,int(src.height*scale)));maxpan=max(0,new.height-bh);pan=int(maxpan*min(1,max(0,(u-.15)/.7)));shot=new.crop((0,pan,bw,pan+bh))
 else:
  zoom=1+0.7*min(1,max(0,(u-.25)/.45));scale=min(bw/src.width,bh/src.height)*zoom;nw,nh=int(src.width*scale),int(src.height*scale);new=src.resize((nw,nh));shot=Image.new('RGB',(bw,bh),'#10141d');shot.paste(new,((bw-nw)//2,int((bh-nh)*.12)))
 im.paste(shot,(box[0],box[1]));d=ImageDraw.Draw(im);pulse=int(130+90*math.sin(u*math.pi)**2);d.rounded_rectangle((box[0]-8,box[1]-8,box[2]+8,box[3]+8),radius=15,outline=(pulse,int(pulse*.82),int(pulse*.45)),width=3)
 d.rounded_rectangle((70,748,1530,817),radius=12,fill='#171b22');d.text((96,767),s[4],font=ft(26,True),fill='#f4e5bd');d.text((70,842),'Existing product demonstration captures; synthetic records. Guided visual tour; no live actions performed.',font=ft(17),fill='#8f99a7');d.text((1420,842),f'{i+1:02d} / 04',font=ft(17),fill='#d8b771');d.rectangle((70,883,1530,887),fill='#242b34');d.rectangle((70,883,70+int(1460*t/duration),887),fill='#d8b771')
 if frame in [45,225,405,585]:im.save(M/f'guided-scene-{i+1}.png')
 proc.stdin.write(im.tobytes())
proc.stdin.close();assert proc.wait()==0
(M/'guided-chapters.json').write_text(json.dumps([{'start':i*12,'title':s[0],'heading':s[1],'description':s[2],'takeaway':s[4],'source':s[3]} for i,s in enumerate(scenes)],indent=2)+'\n')
print('Rendered silent 48-second product-capture walkthrough')
