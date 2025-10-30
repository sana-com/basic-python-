colour=['red','blue','green','blue','yellow','red','blue']
colour_count=colour.count('blue')
colour_index= colour.index('green')
colour_present= 'purple' in colour
new_colour= [x for x in colour if x!='red']
print("the number of times blue present:",colour_count)
print("the index of colour green:",colour_index)
print("is purple present? :",colour_present)
print("list of colour after removing red:",new_colour)
