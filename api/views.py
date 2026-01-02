from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from .models import Tolov, Talaba, Expense, ExpenseCategory, IshHaqqi, Qarzdor, QarzMiqdori
from .serializers import TolovSerializer, ExpenseSerializer, ExpenseCategorySerializer,IshHaqqiSerializer,QarzdorSerializer,QarzMiqdoriSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend



class TolovViewSet(ModelViewSet):
    queryset = Tolov.objects.all().order_by('-sana')
    serializer_class = TolovSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        sana_from = self.request.query_params.get('from')
        sana_to = self.request.query_params.get('to')
        turi = self.request.query_params.get('turi')

        if sana_from and sana_to:
            qs = qs.filter(sana__date__range=[sana_from, sana_to])

        if turi:
            qs = qs.filter(turi=turi)

        return qs

    #ASOSIyJOY(BALANS HISOBI)
    def perform_create(self, serializer):
        tolov = serializer.save()
        talaba = tolov.talaba

        if tolov.turi == 'tolov':
            talaba.balans += tolov.summa
        elif tolov.turi == 'yechib':
            talaba.balans -= tolov.summa

        talaba.save()

    def perform_destroy(self, instance):
        talaba = instance.talaba

        if instance.turi == 'tolov':
            talaba.balans -= instance.summa
        elif instance.turi == 'yechib':
            talaba.balans += instance.summa

        talaba.save()
        instance.delete()

    #jamiyechibolish
    @action(detail=False, methods=['get'])
    def jami_yechib_olish(self, request):
        jami = Tolov.objects.filter(
            turi='yechib'
        ).aggregate(jami=Sum('summa'))['jami'] or 0

        return Response({"jami": jami})

    #oylikstatistika
    @action(detail=False, methods=['get'])
    def oylik_statistika(self, request):
        data = (
            Tolov.objects.filter(turi='yechib')
            .annotate(oy=TruncMonth('sana'))
            .values('oy')
            .annotate(summa=Sum('summa'))
            .order_by('oy')
        )
        return Response(data)





class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by('-date')
    serializer_class = ExpenseSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'payment_type', 'employee']
    search_fields = ['name', 'receiver']

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user)



class IshHaqqiViewSet(ModelViewSet):
    queryset = IshHaqqi.objects.all()
    serializer_class = IshHaqqiSerializer



class QarzdorViewSet(ModelViewSet):
    queryset = Qarzdor.objects.all()
    serializer_class = QarzdorSerializer


class QarzMiqdoriViewSet(ModelViewSet):
    queryset = QarzMiqdori.objects.all()
    serializer_class = QarzMiqdoriSerializer




