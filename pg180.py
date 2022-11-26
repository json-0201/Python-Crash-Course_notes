# 9-10. Imported Restaurant
from pg180_restaurant import Restaurant

rest_1 = Restaurant('chef wong', 'chinese')
rest_2 = Restaurant('vallartas', 'mexican')

rest_1.describe_restaurant()
rest_2.open_restaurant()

# 9-11. Imported Admin
# 9-12. Multiple Modules
from pg180_admin import Admin

myself = Admin('jimmy', 'son')
myself.describe_user()

print(myself.login_attempts)
myself.increment_login_attempts()
print(myself.login_attempts)
myself.reset_login_attempts()
print(myself.login_attempts)

myself.privileges.show_privileges()
