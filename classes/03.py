class chai():
    origin = "india"  # we call them as "property" if we add into the "classes"


print(chai.origin)


chai.is_hot = True
print(chai.is_hot)

# creating object from the  class chai

masala = chai()
print(f"masala {masala.origin}")
print(f"masala {masala.is_hot}")
masala.is_hot = False
print("class:", chai.is_hot)
print(f"masala {masala.is_hot}")
masala.flavour= "masala"
print(masala.flavour)




