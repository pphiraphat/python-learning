# match statement
service = input("้inter your service(1-3)")

match service:
    case "1":print("ถอนเงิน")
    case "2":print("ฝากเงิน")
    case "3":print("สอบถามยอดเงินคงเหลือในบัญชี")
    case " ":print("หมายเลขบริหารไม่ถูกต้อง")
    