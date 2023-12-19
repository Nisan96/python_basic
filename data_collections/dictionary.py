#Dictionary
info = {
    'name': 'Dip',   # 'key' : 'value'
    'email': 'dip@mail.com',
    'phone': ['0177456790','01678996544'],
    'address':{
        'present_address':{
            'House': 'house no:07',
            'Thana': 'Dhanmondi',
            'Division': 'Dhaka',
            'PostalCode': '1200'
        },
        'permanent_address':{
            'Village': 'Bhola',
            'Thana': 'Bhola sadar',
            'District': 'Barisal'
        }
    }
}

print(info['address']['present_address']['Thana'])