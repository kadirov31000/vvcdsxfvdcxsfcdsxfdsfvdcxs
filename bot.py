from pro.accountDetails import AccountDetail
from pro.kadirov import Kadirov
import pro.kadirov 



print("|=================================|")
print("|                                 |")
print("|                                 |")
print("|                                 |")
print("|        lynda free account       |")
print("|                                 |")
print("|                        @kadirov |")
print("|=================================|")


accountdetails = AccountDetail()
info = accountdetails.getInfo()
kadirov = Kadirov(info)
kadirov.genbb()
kadirov.aek()
kadirov.save_info()
kadirov.lynda()
kadirov.logout()