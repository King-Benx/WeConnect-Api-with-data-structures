import random
from flask import session, request, jsonify
from . import users, known_user_ids, known_usernames, businesses, known_business_ids, reviews, known_review_ids
from werkzeug.security import generate_password_hash, check_password_hash


def generate_random_number():
    """ create a random number generator function"""
    return random.randint(1, 1000)


class User:
    """ User class that creates a new user and responsible for operations with the rest of the classes """

    def __init__(self, username, email, password):
        if (username != '' and email != ''
                and password != '') or (username is not None
                                        and email is not None
                                        and password is not None):
            self.id = self.generate_user_id()
            self.username = username
            self.email = email
            self.password_hash = self.generate_password(password)
            self.create_user()
        else:
            raise ValueError('Arguments cannot be empty')

    def create_user(self):
        # creates a new user
        global users
        global known_usernames
        generated_id = self.id
        if self.username not in known_usernames:
            new_user = dict()
            data = [self.username, self.password_hash, self.email]
            new_user[generated_id] = data
            users.append(new_user)
            known_usernames.append({'username': self.username, 'id': self.id})

    def generate_user_id(self):
        """generate a unique user id for a new user"""
        global known_user_ids
        x = generate_random_number()
        if x not in known_user_ids:
            known_user_ids.append(x)
            return x
        else:
            self.generate_user_id()

    @staticmethod
    def generate_password(password):
        """generate a hashed password"""
        return generate_password_hash(password)

    def verify_password(self, password):
        # verify that passwords at login will match
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_user(user_id):
        """ get a user by id"""
        for user in users:
            if user_id in user.keys():
                return user[user_id]

    @staticmethod
    def login(username, password):
        """ authenticate user"""
        for known_user in known_usernames:
            if known_user['username'] == username:
                user_id = known_user['id']
                if check_password_hash(User.get_user(user_id)[1], password):
                    return True
                else:
                    return False

    @staticmethod
    def logout():
        """logout user from system"""
        return True

    @staticmethod
    def get_user_id_by_username(username):
        """ get a user by username"""
        for known_user in known_usernames:
            if known_user['username'] == username:
                user_id = known_user['id']
                return user_id

    @staticmethod
    def reset_password(username, password):
        """reset password to "pass" if the username is existant"""
        global users
        for known_user in known_usernames:
            if known_user['username'] == username:
                default_pass = generate_password_hash(password)
                user_details = User.get_user(
                    User.get_user_id_by_username(username))
                old_password = user_details[1]
                user_details[1] = str(default_pass)
                if old_password != user_details[1]:
                    return True
                else:
                    return False
            else:
                return False


class Business:
    """ Business class that creates a business for a registered user """

    def __init__(self, user_id, name, location, category, description):
        if type(
                user_id
        ) == int and name != '' and name != '' and category != '' and description != '':
            self.id = self.generate_business_id()
            self.user_id = user_id
            self.name = name
            self.location = location
            self.category = category
            self.description = description
            self.create_business()

        else:
            raise ValueError('arguments cannot be empty')

    def generate_business_id(self):
        # generate a business id
        global known_business_ids
        x = generate_random_number()
        if x not in known_business_ids:
            known_business_ids.append(x)
            return x
        else:
            self.generate_business_id()

    def create_business(self):
        # create a business
        global businesses
        global known_business_ids
        new_business = dict()
        generated_id = self.id
        data = [
            self.user_id, self.name, self.location, self.category,
            self.description
        ]
        new_business[generated_id] = data
        businesses.append(new_business)
        return True

    @staticmethod
    def get_business_by_id(business_id):
        # get  business by id
        for business in businesses:
            if business_id in business.keys():
                return business[business_id]

    @staticmethod
    def update_business(user_id,
                        business_id,
                        name='',
                        location='',
                        category='',
                        description=''):
        # authenticate that business_id belongs to user
        global businesses
        global known_business_ids
        if user_id == Business.get_business_by_id(business_id)[0]:
            if name != '' and name != Business.get_business_by_id(
                    business_id)[1]:
                Business.get_business_by_id(business_id)[1] = name
            if location != '' and location != Business.get_business_by_id(
                    business_id)[2]:
                Business.get_business_by_id(business_id)[2] = location
            if category != '' and category != Business.get_business_by_id(
                    business_id)[3]:
                Business.get_business_by_id(business_id)[3] = category
            if description != '' and description != Business.get_business_by_id(
                    business_id)[4]:
                Business.get_business_by_id(business_id)[4] = description
            return True

    @staticmethod
    def get_all_businesses():
        # get  all registered businesses
        business_info = list()
        for business in businesses:
            for key, value in business.items():
                business_info.append({
                    'id': key,
                    'user_id': value[0],
                    'name': value[1],
                    'location': value[2],
                    'category': value[3],
                    'description': value[4]
                })
        return business_info

    @staticmethod
    def delete_business(user_id, id):
        # delete a business by id if you are its user
        global known_business_ids
        global businesses
        if user_id == Business.get_business_by_id(id)[0]:
            for business in businesses:
                if id in business.keys():
                    businesses.remove(business)
                    known_business_ids.remove(id)
                    return True
        else:
            return False


class Review:
    """ Review creates a review by a particular user to a specific business """

    def __init__(self, user_id, business_id, review):
        self.id = self.generate_review_id()
        self.user_id = user_id
        self.business_id = business_id
        self.review = review
        self.create_review()

    def create_review(self):
        # create review
        global reviews
        new_review = dict()
        data = [self.user_id, self.business_id, self.review]
        new_review[self.id] = data
        reviews.append(new_review)
        return True

    def generate_review_id(self):
        # generate a unique id for a review
        global known_review_ids
        x = generate_random_number()
        if x not in known_review_ids:
            known_review_ids.append(x)
            return x
        else:
            self.generate_review_id()

    @staticmethod
    def get_review_by_business(business_id):
        # get a review for a business
        review_details = list()
        if business_id in known_business_ids:
            for review_info in reviews:
                for value in review_info.values():
                    review_detail = {
                        'Author': User.get_user(value[0])[0],
                        'review': value[2]
                    }
                    review_details.append(review_detail)
            return review_details
