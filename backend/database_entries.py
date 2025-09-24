from mainpage_app.models import Users, ItemUnits, Items, Stores, StoreItems


user1 = Users(password='hasanpass', username = 'hasancelik', first_name = 'Hasan', last_name = 'Celik', email = 'hasan.celik@mycompany.com', is_active = True, balance = 0.00)

user2 = Users(password='huseyinpass', username = 'huseyinyilmaz', first_name = 'Huseyin', last_name = 'Yilmaz', email = 'huseyin.yilmaz@mycompany.com', is_active = True, balance = 0.00)

user3 = Users(password='alipass', username = 'alisahin', first_name = 'Ali', last_name = 'Sahin', email = 'ali.sahin@mycompany.com', is_active = True, balance = 0.00)

user4 = Users(password='zeyneppass', username = 'zeynepyildirim', first_name = 'Zeynep', last_name = 'Yildirim', email = 'zeynep.yildirim@mycompany.com', is_active = True, balance = 0.00)

user5= Users(password='fatmapass', username = 'fatmaaydin', first_name = 'Fatma', last_name = 'Aydin', email = 'fatma.aydin@mycompany.com', is_active = True, balance = 0.00)

users = [user1, user2, user3, user4, user5]
for x in users:
    x.save()

item_unit1 = ItemUnits(name = 'kilograms')
item_unit2 = ItemUnits(name = 'liters')
item_unit3 = ItemUnits(name = 'each')
item_unit4 = ItemUnits(name = 'packs')

item_units = [item_unit1, item_unit2, item_unit3, item_unit4]
for x in item_units:
    x.save()

item1 = Items(item_name = 'Elma', description = 'Yerli amasya elmasi', unit_id = 1)
item2 = Items(item_name = 'Muz', description = 'Taze ithal muz', unit_id = 1)
item3 = Items(item_name = 'Ekmek', description = 'Gunluk tas firin ekmegi', unit_id = 3)

items = [item1, item2, item3]
for x in items:
    x.save()



store1 = Stores(store_name = 'Benzin Istasyonu', location = 'Petrol Sokak No 1, Besiktas, Istanbul', contact_email = 'contact@benzinci.com')
store2 = Stores(store_name = 'Teknoloji Dukkani', location = 'Teknoloji Sokak No 2, Sariyer, Istanbul', contact_email = 'contact@techmarket.com')
store3 = Stores(store_name = 'Telefon Operatoru', location = 'Iletisim Sokak No 60, Etiler, Istanbul', contact_email = 'contact@telefoncell.com')
store4 = Stores(store_name = 'Internet Servis Saglayici', location = 'Ucuzasat Sokak No 63, Besiktas, Istanbul', contact_email = 'info@hizlikablolar.com')
store5 = Stores(store_name = 'Supermarket', location = 'Ucuzasat Sokak No 63, Besiktas, Istanbul', contact_email = 'support@supermarket.com')

stores = [store1, store2, store3, store4, store5]
for x in stores:
    x.save()
    
store_item1 = StoreItems(store_id = 5, item_id = 1, stock_quantity = 750.00)
store_item2 = StoreItems(store_id = 5, item_id = 2, stock_quantity = 500.00)
store_item3 = StoreItems(store_id = 5, item_id = 3, stock_quantity = 110.00)

store_items = [store_item1, store_item2, store_item3]
for x in store_items:
    x.save()
