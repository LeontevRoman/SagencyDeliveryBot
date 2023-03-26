import sqlite3

class DataBase:
    def __init__(self, file_path='./db/sagency_referals.db'):
        self.connection = sqlite3.connect(file_path, timeout=7)
        self.cursor = self.connection.cursor()


    def create_user(self, user_id, user_name, referer_id='', invite_link=''):
        check_user = self.cursor.execute("""SELECT user_id FROM bonus WHERE user_id = ?""",
                                              (user_id,)).fetchone()
        if check_user:
            pass
        else:
            self.cursor.execute("""INSERT INTO bonus (user_id, user_name, referer_id, invite_link) VALUES (?,?,?,?)""",
                                (user_id, user_name, referer_id, invite_link))
            self.connection.commit()


    def check_refaral_link(self, user_id):
        check_user_link = self.cursor.execute("""SELECT invite_link FROM bonus WHERE user_id = ?""",
                                               (user_id,)).fetchone()
        if bool(list(check_user_link)[0]):
            return list(check_user_link)[0]
        else:
            return bool(list(check_user_link)[0])


    def create_referal_link(self, user_id, invite_link):
        self.cursor.execute("""UPDATE bonus SET invite_link=? WHERE user_id = ?""", (invite_link, user_id))
        self.connection.commit()


    def update_percent_sale(self, user_id):
        amount_invite_friends = self.cursor.execute("""SELECT percent_sale FROM bonus WHERE user_id = ?""",
                                               (user_id,)).fetchone()
        new_amount_invite_friends = (amount_invite_friends[0]) + 1
        self.cursor.execute("""UPDATE bonus SET percent_sale=? WHERE user_id = ?""", (new_amount_invite_friends, user_id))
        self.connection.commit()
        return new_amount_invite_friends

    def get_percent_sale(self, user_id):
        amount_invite_friends = self.cursor.execute("""SELECT percent_sale, referer_id FROM bonus WHERE user_id = ?""",
                                               (user_id,)).fetchone()
        return int(amount_invite_friends[0])

    def down_percent_sale(self, user_id):
        referer_id = self.cursor.execute("""SELECT referer_id FROM bonus WHERE user_id = ?""",
                                               (user_id,)).fetchone()[0]
        if referer_id:
            amount_invite_friends = self.cursor.execute("""SELECT percent_sale FROM bonus WHERE user_id = ?""",
                                                        (referer_id,)).fetchone()
            new_amount_invite_friends = (amount_invite_friends[0]) - 1
            self.cursor.execute("""UPDATE bonus SET percent_sale=? WHERE user_id = ?""",
                                (new_amount_invite_friends, referer_id))
            self.cursor.execute("""DELETE FROM bonus WHERE user_id = ?""", (user_id,))
            self.connection.commit()
            return new_amount_invite_friends, referer_id
        else:
            self.cursor.execute("""DELETE FROM bonus WHERE user_id = ?""", (user_id,))
            self.connection.commit()
            return 0, 0