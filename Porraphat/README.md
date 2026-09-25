# วิธีอัพขึ้น GitHub (ทำผ่าน VS Code)

**ไฟล์ที่ต้องมี:** `index.html` และ `song.mp3` ต้องอยู่โฟลเดอร์เดียวกัน

1. เปิดโฟลเดอร์นี้ใน VS Code
2. (ถ้าอยากใส่รูปเธอ) เอาไฟล์รูปชื่อ `her-photo.jpg` มาไว้โฟลเดอร์เดียวกัน แล้วเปิด `index.html` หาโค้ดส่วน `<div class="photo-frame">` แก้จาก
   `<span>📷<br>ใส่รูปเธอตรงนี้นะ</span>`
   เป็น
   `<img src="her-photo.jpg" alt="รูปเธอ">`
3. เปิด Terminal ใน VS Code แล้วรัน:
   ```
   git init
   git add .
   git commit -m "ง้อสาว"
   git branch -M main
   git remote add origin https://github.com/USERNAME/REPO-ชื่อ.git
   git push -u origin main
   ```
   (สร้าง repo เปล่าบน github.com ก่อน แล้วเอาลิงก์มาแทน URL ด้านบน)
4. ไปที่ repo บน GitHub → Settings → Pages → เลือก branch `main` / folder `root` → Save
5. รอ 1-2 นาที จะได้ลิงก์ประมาณ `https://USERNAME.github.io/REPO-ชื่อ/` ส่งลิงก์นี้ให้เธอได้เลย

**เพลง:** ใช้ไฟล์ที่แนบมาเป็น `song.mp3` ถ้าอยากเปลี่ยนเพลง เอาไฟล์ mp3 ใหม่มาแทนแล้วตั้งชื่อ `song.mp3` เหมือนเดิม (หรือแก้ชื่อไฟล์ใน `index.html` ตรง `<audio ... src="song.mp3">`)

**แก้ข้อความ:** เปิด `index.html` แล้วแก้ประโยคในแท็ก `<p class="message">` และ `<h1 class="headline">` ให้เป็นคำพูดของตัวเองได้เลย
