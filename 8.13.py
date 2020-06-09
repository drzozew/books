def build_profile(first, last, **user_info):
    '''Builds of dicionary with info'''
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info


user_profil = build_profile('Badzi', "Kara", loc='Kart', cel='Python')
print(user_profil)
