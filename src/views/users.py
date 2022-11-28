from http import HTTPStatus
from flask import views, request
from marshmallow.validate import ValidationError

from utilities import db
from models import User
from schemas import UserSchema


class UserViewSet(views.MethodView):
    model = User
    schema_class = UserSchema
    lookup_field = "id"
    lookup_url_kwarg = "id"

    def post(self, *arg, **kwargs):
        """Post : It will post data"""

        schema = self.schema_class()
        try:
            instance = schema.load(request.json)
        except ValidationError as e:
            return e.messages, HTTPStatus.BAD_REQUEST
        db.session.add(instance)
        db.session.commit()
        return schema.dump(instance), HTTPStatus.OK

    def get_object(self, *args, **kwargs):
        """Get Obejct : it will fetch the details of a specific user"""

        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: kwargs[lookup_url_kwarg]}
        obj = self.model.query.filter_by(**filter_kwargs).first()
        return obj

    def get(self, *args, **kwargs):
        """GET : It will retrieve specific as well as all records of database"""

        if self.lookup_url_kwarg not in kwargs:
            instance = self.model.query.all()
            schema = self.schema_class(many=True)
            return schema.dump(instance), HTTPStatus.OK

        instance = self.get_object(*args, **kwargs)
        schema = self.schema_class()
        if not instance:
            return {"message": "Details not found"}, HTTPStatus.NOT_FOUND
        return schema.dump(instance), HTTPStatus.OK

    def delete(self, *args, **kwargs):
        """Delete: It will delete the specific user"""

        instance = self.get_object(*args, **kwargs)
        if not instance:
            return {"message": "Record Not found"}, HTTPStatus.NOT_FOUND
        schema = self.schema_class()
        db.session.delete(instance)
        db.session.commit()

        return {"message": "Record is deleted"}

    def put(self, *args, **kwargs):
        """ Put : It will change the full details of a specific id """

        instance = self.get_object(*args, **kwargs)
        if not instance:
            return {"message": "Record Not found"}, HTTPStatus.NOT_FOUND
        schema = self.schema_class()
        try:
            instance = schema.load(request.json, instance=instance)
        except ValidationError as e:
            return e.messages, HTTPStatus.BAD_REQUEST
        db.session.add(instance)
        db.session.commit()

        return schema.dump(instance), HTTPStatus.OK

    def patch(self, *args, **kwargs):
        """Patch: It  will change some fields of the model"""

        instance = self.get_object(*args, **kwargs)
        if not instance:
            return {"message": "Record Not found"}, HTTPStatus.NOT_FOUND
        schema = self.schema_class()
        try:
            instance = schema.load(request.json, instance=instance, partial=True)
        except ValidationError as e:
            return e.messages, HTTPStatus.BAD_REQUEST
        db.session.add(instance)
        db.session.commit()

        return schema.dump(instance), HTTPStatus.OK
