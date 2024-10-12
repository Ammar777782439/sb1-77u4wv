from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from store.models import Order, Product
from django.db.models import Sum, F

def generate_sales_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="sales_report.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.setFont("Helvetica", 12)
    p.drawString(100, 750, "تقرير المبيعات")

    y = 700
    for order in Order.objects.filter(is_completed=True):
        p.drawString(100, y, f"طلب رقم: {order.id} - التاريخ: {order.date_ordered}")
        y -= 20
        for item in order.orderitem_set.all():
            p.drawString(120, y, f"{item.product.name} - الكمية: {item.quantity} - السعر: {item.product.price}")
            y -= 20
        y -= 10

    p.showPage()
    p.save()
    return response

def generate_inventory_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="inventory_report.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.setFont("Helvetica", 12)
    p.drawString(100, 750, "تقرير المخزون")

    y = 700
    for product in Product.objects.annotate(total_sold=Sum('orderitem__quantity')):
        p.drawString(100, y, f"{product.name} - السعر: {product.price} - الكمية المباعة: {product.total_sold or 0}")
        y -= 20

    p.showPage()
    p.save()
    return response