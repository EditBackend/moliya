from rest_framework import serializers
from .models import Talaba, Tolov,  Expense, ExpenseCategory
from .models import IshHaqqi, Qarzdor, QarzMiqdori


class TalabaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talaba
        fields = '__all__'


class TolovSerializer(serializers.ModelSerializer):
    talaba_ismi = serializers.CharField(
        source='talaba.full_name',
        read_only=True
    )

    class Meta:
        model = Tolov
        fields = [
            'id',
            'talaba',
            'talaba_ismi',
            'summa',
            'turi',
            'izoh',
            'xodim',
            'sana',
        ]





class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    employee_name = serializers.CharField(source='employee.username', read_only=True)

    class Meta:
        model = Expense
        fields = [
            'id',
            'date',
            'category',
            'category_name',
            'name',
            'receiver',
            'payment_type',
            'amount',
            'employee',
            'employee_name',
            'created_at'
        ]


class IshHaqqiSerializer(serializers.ModelSerializer):
    class Meta:
        model = IshHaqqi
        fields = '__all__'


class QarzMiqdoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = QarzMiqdori
        fields = '__all__'


class QarzdorSerializer(serializers.ModelSerializer):
    qarzlar = QarzMiqdoriSerializer(many=True, read_only=True)

    class Meta:
        model = Qarzdor
        fields = '__all__'
