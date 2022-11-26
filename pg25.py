#2-3. Personal Message
name = 'Jimmy'
message = f'Hello {name}, would you like to learn some Python today?'
print(message)

#2-4. Name Cases
name2 = 'jImMy SoN'
name2_lower = name2.lower()
name2_upper = name2.upper()
name2_title = name2.title()

print(name2_lower)
print(name2_upper)
print(name2_title)

#2-5. Famous Quote
print('Bruce Lee once said, "Empty your mind, be formless. Shapeless. Like water"')

#2-6. Famous Quote 2
famous_person = 'Bruce Lee'
famous_quote = 'Empty your mind, be formless. Shapeless. Like water'
message = f'{famous_person} once said, "{famous_quote}"'
print(message)

#2-7 Stripping Names
name3 = '   \tBruce Lee   '
print(name3)

print(name3.lstrip())
print(name3.rstrip())
print(name3.strip())
