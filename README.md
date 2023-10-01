# Posing-as-a-detective
Posing as a detective : มินิโปรเจ็คสำหรับฝึกการ request api และการกรองข้อมูล

## ก่อนเริ่ม:
- ทำการ `Fork` ให้เรียบร้อยปุ่มตามภาพด้านล่าง
  
<p align="center" >
<img src="https://media.discordapp.net/attachments/585068497495654413/1157607458785738823/tvcerWg.png?ex=65193975&is=6517e7f5&hm=d8679cce83c666bd2b3b601b77b666eacf1b2df1dd73d1cba18f7290032f6b89&=">
</p>

- ตั้งชื่อ repo ใหม่ (ไม่จำเป็น) จากนั้นกดปุ่ม `Create Fork`

<p align="center" >
<img src="https://cdn.discordapp.com/attachments/372372440334073859/1156569568760823858/image.png?ex=651572d9&is=65142159&hm=33d89652d11f893a1a48743efa9ac68a0a4f5330bb9c3f01a9d2e4245b3c4139&">
</p>

- ไปที่ปุ่ม `Code` คัดลอกลิงก์ดังรูป

<p align="center" >
<img align="center" src="https://cdn.discordapp.com/attachments/372372440334073859/1156570821775601796/305y5IV.png?ex=65157403&is=65142283&hm=3bb6a5c0537813df810ce84d3a25616e964d3e0d7581b5cc4bbaf4fe6f8aa2f1&">
</p>

- จากนั้นไปที่ Terminal (macOS)หรือ cmd (Windows) และทำการ cd ไปยัง drive ที่จะเก็บงานก่อน เมื่อเสร็จแล้ว
- จากนั้นใช้คำสั่งต่อไป
```
git clone <url ที่คัดลอกมา>
```
```
cd Posing-as-a-detective
```
```
code .
```

  
* `code .` คือกรณีใช้ vscode ใช้ VSCode

### การบันทึกที่นอกจากกด save
คือการ commit เป็นการสร้างเวอร์ชันให้กับโค้ดที่เรากำลังเขียน
- วิธีการ commit ใน VSCode

<p align="center" >
<img src="https://cdn.discordapp.com/attachments/585068497495654413/1157597417580003368/gamedfdsf.gif?ex=6519301b&is=6517de9b&hm=616c4e91ac975f1feed0e2d3c82e9c85e6764e860089544e5e20113f392e72b3&">
</p>

### รู้ก่อนเริ่มขั้นสุดท้าย

- ทุกครั้งที่เขียนแต่ละฟังก์ชั่นเสร็จให้ทำการ `commit` ทุกครั้ง
- จากนั้นก็ทำการ `Pull Request` โดยไปที่หน้า repo ของคุณที่พึ่ง `Fork` ไปจากนั้นทำตามภาพ

<div align="center" >

![](https://cdn.discordapp.com/attachments/372372440334073859/1156573259232448552/6f14jIy.png?ex=65157649&is=651424c9&hm=974ba577b6848d81f98f1d051617f7a071dd6a6596cf2709a56894602ea88db2&)

</div>

- เลือก `New pull request` 

<div align="center" >

![](https://cdn.discordapp.com/attachments/372372440334073859/1156573519803596910/image.png?ex=65157687&is=65142507&hm=a650722f6188d36455095de634f2d1decc76d7263d4615b4f2d55b45fb132398&)

</div>

- เลือก `Create pull request`

<div align="center" >

![](https://cdn.discordapp.com/attachments/372372440334073859/1156573856362922076/image.png?ex=651576d7&is=65142557&hm=4e539be01ec4ef80856b0865ab87ab4373da105c7197ed844c513657d7752b47&)

</div>

- ตั้งชื่อสิ่งที่เพิ่มเข้ามาพยายามบอกว่าคุณเขียนโค้ดอะไรเสร็จแล้ว จากนั้นเลือก `Create pull request` อีกครั้ง

<div align="center" >
  
![](https://cdn.discordapp.com/attachments/372372440334073859/1156574064001953802/image.png?ex=65157708&is=65142588&hm=3c2346880545bebaef1dd50412c9efbb2c098df7ac3b39f8e41a93e617a081e4&)

</div>

- เสร็จจากนั้นรอเจ้าของโครงการ commit


## มาเริ่มกัน
### ข้อมูลที่ตำรวจอยากรู้:

1. มีผู้ใดมีสีผมสีดำ (black hair) และสีตาสีน้ำตาล (brown eyes) บ้าง?
- John Doe
- Daniel Thompson

2. มีผู้ใดมีอายุมากที่สุด?
- 45

3. มีผู้หญิงทั้งหมดกี่คน?
- 5

4. มีผู้ชายที่มีส่วนสูงตั้งแต่ 180 เซนติเมตรขึ้นไปและน้ำหนักตั้งแต่ 80 กิโลกรัมขึ้นไปทั้งหมดกี่คน?
- 2 คน

5. มีผู้ใดมีประวัติส่วนตัวเป็นคนสูบบุหรี่ (smokes cigarettes) บ้าง?
- Daniel Thompson


6. ผู้แจ้งเบาะแสบอกว่าพบชายอายุกลางคนผมดำพบรอยสักบนแขนขวา (tattoo on right forearm) ขโมยของแล้วหลบหนีไปโดยขับรถยนต์หนีออกไประหว่างนั้นผู้แจ้งเบาะแสได้สบตามกับชายดังกล่าวพบว่ามีตาสีน้ำเงิน คุณคือว่าชายนนั้นคือใครในฐานข้อมูลของเรา
- Matthew Davis

## สิ่งที่คุณต้องทำอันดับแรก
- ต้องทำการเชื่อมต่อกับฐานข้อมูลผู้ต้องสงสัยก่อนโดยใช้ `requests` ซึ่ง `import` ให้แล้วในไฟล์ `posing_a_detective.py` 
- ไปเขียนโค้ดต่อในฟังก์ชัน `pull_database_suspect()` เพื่อเชื่อม API ก่อนอันดับแรก 
- แล้วแสดงผลข้อมูลออกมาแล้วทำตามโจทย์จากทางตำรวจแล้วเอาคำตอบไปเขียนใต้โจทย์คำถามในไฟล์ `README.md` 
- โดยลิงก์ฐานข้อมูลคือ `https://ppythonbasic.github.io/apis/suspects.json`
- ในการรันให้ใช้คำสั่งสำหรับ macOS
```
python3 main.py
```
- ในการรันให้ใช้คำสั่งสำหรับ Windows
```
python main.py
```
> :warning: ไฟล์ `main.py` ใช้สำหรับรันผลลัพธ์พยายามแก้ไขแค่ในไฟล์ `posing_a_detective.py`

## การใช้ requests และ json แบบเร็วๆ
```
response = requests.get(url).text #สำหรับดึงข้อมูล api
response_json = json.loads(response) #เพื่อแปลงข้อมูลจากข้อความมาเป็น dict
response_json['name'] #ตัวอย่างการเข้าถึงข้อมูลแบบ dict เช่น {'name': 'John'}
response_json[0] #ตัวอย่างการเข้าถึงข้อมูลแบบ list เช่น ['ice','water']
```
