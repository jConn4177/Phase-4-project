from flask_restful import Resource, reqparse


class UserResource(Resource):
    def get(self, user_id):
        from server.models.user import User  # Import User within the function
        user = User.query.get(user_id)
        if user:
            return user.to_dict(), 200
        else:
            return {"message": "User not found"}, 404

    def post(self):
        from server.models.user import User  # Import User within the function
        from server.app import db  # Import db within the function
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, required=True)
        parser.add_argument("email", type=str, required=True)
        args = parser.parse_args()

        new_user = User(username=args["username"], email=args["email"])
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User created successfully"}, 201
