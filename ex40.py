import ex40_import

class MyStuff(object):
    def __init__(self):
        print("Hello")
        self.tangerine = " And now a thousand years between."

    def apple(self):
        print("I AM CLASSY APPLES!")
        print(object)

print('-'*40)
thing = MyStuff()
thing.apple()
print(thing.tangerine)


print('-'*40)
bag = {'apple' : "I am Apples"}
print(bag['apple'])

print('-'*40)
ex40_import.apple()


print('-'*40)
bag['apple']
print(ex40_import.apple())
print(ex40_import.tangerine)

#dict style
print(ex40_import.mystuff['apple'])
