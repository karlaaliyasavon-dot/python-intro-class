#what data the program is actually pulling from
#STILL need to get it to properly reference
import AnonyMate
from simple_anonymizer import Anonymizer
from cryptography.fernet import Fernet
from decimal import Decimal
import datetime
import json

#starting the anonymizer and the encryption
anon = Anonymizer()
crypto = Fernet(Fernet.generate_key())

#profile information
profiles =  [
    {'job': 'Agricultural engineer', 'company': 'Phillips-Johnson', 'ssn': '055-51-3629',
     'residence': '1107 Brian Coves\nSouth Jessica, UT 66862',
     'current_location': (Decimal('-81.6575675'), Decimal('111.794874')),
     'blood_group': 'B+', 'website': ['https://hurley.com/', 'http://www.baker.info/',
                                      'http://silva-jones.com/', 'https://www.mathews.com/'],
     'username': 'nelson', 'name': 'Oscar Newman', 'sex': 'M',
     'address': '2574 Scott Manors\nPort Aprilfort, MI 13337',
     'mail': 'wgraham@hotmail.com', 'birthdate': datetime.date(1927, 1, 19)},
    {'job': 'Engineer, civil (consulting)', 'company': 'Guzman Inc', 'ssn': '457-09-3674',
     'residence': '8014 Lambert Ways Apt. 285\nSouth Briannaside, KS 13217',
     'current_location': (Decimal('61.686331'), Decimal('-42.036583')),
     'blood_group': 'A-', 'website': ['http://gregory-martin.org/', 'http://tanner.org/',
                                      'https://www.carr.org/'],
     'username': 'liking', 'name': 'Jeremy Wilson', 'sex': 'M',
     'address': '9375 Thomas Alley Suite 536\nNorth Darren, AZ 22956',
     'mail': 'hdeleon@hotmail.com', 'birthdate': datetime.date(1996, 10, 12)},
    {'job': 'Information officer', 'company': 'Green Inc', 'ssn': '230-42-2169',
     'residence': 'Unit 6625 Box 0858\nDPO AE 52466',
     'current_location': (Decimal('-78.802646'), Decimal('-47.996111')),
     'blood_group': 'A-', 'website': ['https://www.watkins.com/', 'http://johnson.org/'],
     'username': 'astrophysicist', 'name': 'Kenneth Rhodes', 'sex': 'M',
     'address': '7994 Pearson Square\nHannahmouth, FM 16699',
     'mail': 'sonya72@hotmail.com', 'birthdate': datetime.date(2003, 6, 15)},
    {'job': 'Contracting civil engineer', 'company': 'Smith-Williamson', 'ssn': '796-76-1297',
     'residence': '0041 Brittany Mountains\nNorth Harryshire, MN 69202',
     'current_location': (Decimal('66.422320'), Decimal('107.124001')),
     'blood_group': 'AB+', 'website': ['http://www.nolan.com/'],
     'username': 'paraphilias', 'name': 'Nicole Richardson', 'sex': 'F',
     'address': '303 Wong Trafficway Suite 883\nLake Kiara, MN 78039',
     'mail': 'andrew33@gmail.com', 'birthdate': datetime.date(2003, 9, 7)},
    {'job': 'Engineer, technical sales', 'company': 'Moody-Meza', 'ssn': '574-63-6422',
     'residence': '74438 Moore Fall\nSouth Andrew, GA 64257',
     'current_location': (Decimal('38.089195'), Decimal('35.459581')),
     'blood_group': 'A+', 'website': ['https://brooks-moore.com/'],
     'username': 'xlewis', 'name': 'Gary Gamble', 'sex': 'M',
     'address': '9929 Henderson Branch Suite 961\nLake Mary, AL 36478',
     'mail': 'ambercordova@yahoo.com', 'birthdate': datetime.date(1968, 8, 19)}
]

class AnonyMate:

    def __init__(self, key: bytes = None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_profile(self, profile: dict) -> bytes:

        """
        Encrypts the full profile dict as a UTF-8 JSON string
        """

        #the different profile fields
        profile["address"] = anon.anonymize_text(profile["address"])
        profile["mail"] = anon.anonymize_text(profile["mail"])
        profile["residence"] = anon.anonymize_text(profile["residence"])

        serializable = {}
        for k, v in profile.items():

            if isinstance(v, (Decimal, datetime.date)):
                serializable[k] = str(v)
            else:
                serializable[k] = v

        data = json.dumps(serializable).encode("utf-8")
        return self.cipher.encrypt(data)

    def decrypt_profile(self, encrypted: bytes) -> dict:
        """
        Decrypts the encrypted profile back to a dict.
        """

        decrypted =self.cipher.decrypt(encrypted)
        profile = json.loads(decrypted.decode("utf-8"))
        return profile

    def query_profile(self, encrypted_profiles, index: int, field: str):
        """
        Allows the user to query specific field from an encrypted profile:
        Allowed fields: name, birthdate, sex, blood_group
        """
        allowed_fields = {"name", "birthdate", "sex", "blood_group"}

        if field not in allowed_fields:
            raise ValueError(f"Invalid field: '{field}'. Allowed: {allowed_fields}")

        if index < 0 or index >= len(encrypted_profiles):
            raise IndexError("Profile index out of range.")

        decrypted = self.decrypt_profile(encrypted_profiles[index])
        return decrypted[field]

    if __name__ == "__main__":
        anonymate = AnonyMate()
        encrypted_profiles = []
        for profile in profiles:
            encrypted_profiles.append(
                anonymate.encrypt_profile(profile))

        print("Querying Profile 0:")
        print("Name:", anonymate.query_profile(encrypted_profiles, 0, "name"))
        print("DoB:", anonymate.query_profile(encrypted_profiles, 0, "birthdate"))
        print("Sex", anonymate.query_profile(encrypted_profiles, 0, "sex"))
        print("Blood Group:", anonymate.query_profile(encrypted_profiles, 0, "blood_group"))

        index =int(input("Enter the desired index: "))
        field = input("Enter field (name, birthdate, sex, blood_group): ")

        print(anonymate.query_profile(encrypted_profiles, index, field))
