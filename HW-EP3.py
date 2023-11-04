tilecolor = {'เหรียญทอง':200, 'เหรียญเงิน':100, 'เหรียญทองแดง':90}

print('------โปรแกรมคำนวณเหรียญ by Rich ------')
try:
    tiles = int(input('คุณต้องการเหรียญทั้งหมดกี่เหรียญ: '))
    row = int(input('1 คุณต้องการกีเหรียญ: '))  # 3 กระเบื้องต่อแถว
    color = input('เหรียญสีอะไร? [เหรียญทอง / เหรียญเงิน / เหรียญทองแดง]: ')
except:
    print('กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น!')
    tiles = int(input('คุณต้องการทั้งหมดกี่เหรียญ: '))
    row = int(input('1 คุณต้องการเหรียญกี่เหรียญ: '))
    color = input('กระเบื้องสีอะไร? [เหรียญทอง / เหรียญเงิน / เหรียญทองแดง]: ')

print('-------Calculate-------')
total_row = tiles // row
remain_tiles = tiles % row

#print(total_row,remain_tiles)

buy_more = row - remain_tiles

print(f'มีเหรียญทั้งหมด: {tiles} เหรียญ')
print(f'1 แถวปูกระเบื้องได้ {row} เหรียญ')
print('------คำนวณ------')
print('ต้องปูกระเบื้องทั้งหมด {} เหรียญ'.format(total_row))
print('เหลือกระเบื้องที่ยังไม่ได้ปูเต็มแถว {} เหรียญ'.format(remain_tiles))
print('ลูกค้าต้องซื้อกระเบื้องเพิ่ม {} เหรียญ'.format(buy_more))
print('ยอดรวมทั้งหมดที่ต้องซื้อกระเบื้องเพิ่ม: {} เหรียญ'.format(buy_more * tilecolor[color]))
#ลูกค้าต้องซื้อเหรียญเพิ่มกี่เหรียญ
              