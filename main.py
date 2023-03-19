import classes_objects
def main():
    print("1) Ayakkabı\n 2) Saat\n 3) Kıyafet\n 4) Çanta\n\n Lütfen alışveriş yapmak istediğiniz kategoriyi yanındaki numaralardan faydalanarak seçiniz.")
    user_choice=input("Hangi tür eşya alışverişi yapacaksınız:")
    if user_choice == 1:
        print("1) Erkek\n 2) Kadın")
        which_gender = input("Hangi cinsiyet için alışveriş yapacaksınız?")
        if which_gender == 1:
            print("1) Spor Ayakkabı\n 2) Günlük Ayakkabı\n 3) Yürüyüş Ayakkabısı\n 4) Krampon\n 5) Bot")
        shoes_choice=input("Hangi ayakkabı modelini istiyorsunuz?")
        if shoes_choice == 1:
            print(f"1) {classes_objects.men_shoes1.name}, 2) {classes_objects.men_shoes2.name}, 3) {classes_objects.men_shoes3.name}")
            sport_shoes_choice=input("Hangi spor ayakkabı modelini almak istiyorsunuz?\n")
            if sport_shoes_choice == 1:
                print(f"Ürün adı: {classes_objects.men_shoes1.name}\n Ürün açıklaması: {classes_objects.men_shoes1.description}\n Ürün tipi: {classes_objects.men_shoes1.type}\n Ürün Cinsiyeti: {classes_objects.men_shoes1.gender}\n Ürün Fiyatı: {classes_objects.men_shoes1.price}")
            elif sport_shoes_choice == 2:
                print(f"Ürün adı: {classes_objects.men_shoes2.name}\n Ürün açıklaması: {classes_objects.men_shoes2.description}\n Ürün tipi: {classes_objects.men_shoes2.type}\n Ürün Cinsiyeti: {classes_objects.men_shoes2.gender}\n Ürün Fiyatı: {classes_objects.men_shoes2.price}")    
            elif sport_shoes_choice == 3:
                print(f"Ürün adı: {classes_objects.men_shoes1.name}\n Ürün açıklaması: {classes_objects.men_shoes1.description}\n Ürün tipi: {classes_objects.men_shoes3.type}\n Ürün Cinsiyeti: {classes_objects.men_shoes3.gender}\n Ürün Fiyatı: {classes_objects.men_shoes3.price}")
        elif shoes_choice == 2:
            print(f"1) {classes_objects.men_shoes4.name}, 2) {classes_objects.men_shoes5.name}, 3) {classes_objects.men_shoes6.name}")
            casual_shoes_choice =input("Hangi günlük ayakkabı modelini almak istiyorsunuz?\n")
            if casual_shoes_choice == 1:
                print(f"Ürün adı: {classes_objects.men_shoes4.name}\n Ürün açıklaması: {classes_objects.men_shoes4.description}\n Ürün tipi: {classes_objects.men_shoes4.type}\n Ürün Cinsiyeti: {classes_objects.men_shoes4.gender}\n Ürün Fiyatı: {classes_objects.men_shoes4.price}")
            elif casual_shoes_choice == 2:
                print(f"Ürün adı: {classes_objects.men_shoes5.name}\n Ürün açıklaması: {classes_objects.men_shoes5.description}\n Ürün tipi: {classes_objects.men_shoes5.type}\n Ürün Cinsiyeti: {classes_objects.men_shoes5.gender}\n Ürün Fiyatı: {classes_objects.men_shoes5.price}")    
            elif casual_shoes_choice == 3:
                print(f"Ürün adı: {classes_objects.men_shoes6.name}\n Ürün açıklaması: {classes_objects.men_shoes6.description}\n Ürün tipi: {classes_objects.men_shoes6.type}\n Ürün Cinsiyeti: {classes_objects.men_shoes6.gender}\n Ürün Fiyatı: {classes_objects.men_shoes6.price}")
        elif shoes_choice == 3:
            print(f"1) {classes_objects.men_shoes7.name}, 2) {classes_objects.men_shoes8.name}, 3) {classes_objects.men_shoes9.name}")
            walking_shoes_choice = input("Hangi yürüyüş ayakkabı modelini istiyorsunuz?")
            if walking_shoes_choice == 1:
                print(f"Ürün adı: {classes_objects.men_shoes7.name}\n Ürün açıklaması: {classes_objects.men_shoes7.description}\n Ürün tipi: {classes_objects.men_shoes7.type}\n Ürün Cinsiyeti: {classes_objects.men_shoes7.gender}\n Ürün Fiyatı: {classes_objects.men_shoes7.price}")
            elif walking_shoes_choice == 2:
                print(f"Ürün adı: {classes_objects.men_shoes8.name}\n Ürün açıklaması: {classes_objects.men_shoes8.description}\n Ürün tipi: {classes_objects.men_shoes8.type}\n Ürün Cinsiyeti: {classes_objects.men_shoes8.gender}\n Ürün Fiyatı: {classes_objects.men_shoes8.price}")    
            elif walking_shoes_choice == 3:
                print(f"Ürün adı: {classes_objects.men_shoes9.name}\n Ürün açıklaması: {classes_objects.men_shoes9.description}\n Ürün tipi: {classes_objects.men_shoes9.type}\n Ürün Cinsiyeti: {classes_objects.men_shoes9.gender}\n Ürün Fiyatı: {classes_objects.men_shoes9.price}")
        elif shoes_choice == 4:
            print(f"1) {classes_objects.men_shoes10.name}, 2) {classes_objects.men_shoes11.name}, 3) {classes_objects.men_shoes12.name}")
            spike_choice = input("Hangi krampon modelini almak istiyorsunuz?")
            if spike_choice == 1:
                print(f"Ürün adı: {classes_objects.men_shoes10.name}\n Ürün açıklaması: {classes_objects.men_shoes10.description}\n Ürün tipi: {classes_objects.men_shoes10.type}\n Ürün Cinsiyeti: {classes_objects.men_shoes10.gender}\n Ürün Fiyatı: {classes_objects.men_shoes10.price}")
            elif spike_choice == 2:
                print(f"Ürün adı: {classes_objects.men_shoes11.name}\n Ürün açıklaması: {classes_objects.men_shoes11.description}\n Ürün tipi: {classes_objects.men_shoes11.type}\n Ürün Cinsiyeti: {classes_objects.men_shoes11.gender}\n Ürün Fiyatı: {classes_objects.men_shoes11.price}")    
            elif spike_choice == 3:
                print(f"Ürün adı: {classes_objects.men_shoes12.name}\n Ürün açıklaması: {classes_objects.men_shoes12.description}\n Ürün tipi: {classes_objects.men_shoes12.type}\n Ürün Cinsiyeti: {classes_objects.men_shoes12.gender}\n Ürün Fiyatı: {classes_objects.men_shoes12.price}")
        elif shoes_choice == 5:
            print(f"1) {classes_objects.men_shoes13.name}, 2) {classes_objects.men_shoes14.name}, 3) {classes_objects.men_shoes15.name}")
            boots_choice=input("Hangi bot modelini almak istiyorsunuz?")
            if boots_choice == 1:
                print(f"Ürün adı: {classes_objects.men_shoes13.name}\n Ürün açıklaması: {classes_objects.men_shoes13.description}\n Ürün tipi: {classes_objects.men_shoes13.type}\n Ürün Cinsiyeti: {classes_objects.men_shoes13.gender}\n Ürün Fiyatı: {classes_objects.men_shoes13.price}")
            elif boots_choice == 2:
                print(f"Ürün adı: {classes_objects.men_shoes14.name}\n Ürün açıklaması: {classes_objects.men_shoes14.description}\n Ürün tipi: {classes_objects.men_shoes14.type}\n Ürün Cinsiyeti: {classes_objects.men_shoes14.gender}\n Ürün Fiyatı: {classes_objects.men_shoes14.price}")    
            elif boots_choice == 3:
                print(f"Ürün adı: {classes_objects.men_shoes15.name}\n Ürün açıklaması: {classes_objects.men_shoe15.description}\n Ürün tipi: {classes_objects.men_shoes15.type}\n Ürün Cinsiyeti: {classes_objects.men_shoes15.gender}\n Ürün Fiyatı: {classes_objects.men_shoes15.price}")           
            