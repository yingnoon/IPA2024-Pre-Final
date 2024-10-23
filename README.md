# IPA2024-Pre-Final

## Instruction

1. Fork repository นี้ไปยัง GitHub repository ของตนเอง
2. ทำการ Clone repository จาก GitHub repository ของตนเอง ไปยัง GitHub/local repository ในเครื่องของตนเอง
3. ดำเนินการเขียนโปรแกรมตามดังรูปแบบที่เคยทำใน https://github.com/chotipat/NPA2023-Final โดยมีการเปลี่ยนแปลงโจทย์ดังที่กำหนดด้านล่างนี้
4. ให้ commit และเขียน commit message ที่ดี อยู่เป็นระยะ
5. เมื่อทำเสร็จแล้ว ให้ส่งข้อมูลชื่อ นามสกุล GitHub URL และตอบคำถามลงใน Google Form ที่ https://forms.gle/6DcZChDKQAUXCPCU9 ภายในเวลา 15:30 น.

เปลี่ยนแปลงโจทย์ดังนี้

1. ทำตามโจทย์ NPA2023 Final โดยไฟล์หลัก ipa2024_final.py ไม่ให้ใช้ Hardcode Token ให้เก็บ Token ใน Environment variable
2. สร้าง Python Virtual Environment และ install libraries ที่ต้องใช้ลงใน Virtual environment และสร้าง requirements.txt เพื่อเก็บ List ของ Libraries ที่ต้องใช้ทั้งหมด และ commit และ push มาใน GitHub ด้วย ไม่ต้อง push virtual environment และ libraries ให้ push แต่ requirements.txt
3. ให้ใช้ Netmiko/TextFSM เพื่อกำหนดค่า Description ของ Loopback Interface ที่สร้างมา
4. ปรับปรุง ipa2024_final.py ให้เพิ่มรับ command desc เพื่อตั้งค่า description โดยใช้ netmiko/TextFSM ที่เขียนไว้ในข้อ เช่น เมื่อได้รับข้อความ "/66070123 desc myloopback" ให้ตั้งค่า description ของ interface loopback 66070123 ให้เป็นข้อความ myloopback และส่งผลการทำไปยัง Webex Team room IPA2024 ว่าการตั้งค่าสำเร็จหรือไม่สำเร็จ
5. ใช้ ansible ทำ Lab เพื่อตั้งค่า IPv6 ของ Interface loopback เช่น เมื่อได้รับข้อความ "/66070123 ipv6 FE80::100" ให้ใช้ ansible playbook ไปตั้งค่า IPv6 Loopback 66070123 เป็น FE80::100/64 และทำการยืนยันโดยส่งกลับค่าไปยัง Webex Team room IPA2024 ว่าการตั้งค่าสำเร็จหรือไม่สำเร็จ

***ให้ commit ไฟล์ที่เกี่ยวข้อง และ push ไปที่ GitHub ด้วย***

***อาจจะต้องเขียน Code ในส่วนอื่นๆเอง ที่ไม่ได้ระบุไว้ใน <!!! !!!>***

