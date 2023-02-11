import json 
import stripe
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.template import loader 
from django.http import HttpResponse, JsonResponse
from .models import Item
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY



def list_item(request):
	items = Item.objects.all()

	context = {'items':items}

	template = loader.get_template('items/list_item.html')
	return HttpResponse(template.render(context, request))

def detail_item(request, id):
	item = get_object_or_404(Item, id=id)
	context = {
		'item':item,
	}
	template = loader.get_template('items/detail_item.html')
	return HttpResponse(template.render(context, request))

@csrf_exempt
def checkout(request, id):
	item = get_object_or_404(Item, id=id)
	amount = int(item.price*100)
	session = stripe.checkout.Session.create(
	    line_items=[{
	      'price_data': {
	        'currency': 'rub',
	        'product_data': {
	          'name': item.name,
	        },
	        'unit_amount':amount,
	      },
	      'quantity': 1,
	    }],
	    mode='payment',
	    success_url= request.build_absolute_uri(reverse("items:success"))+'?session_id={CHECKOUT_SESSION_ID}',
	    cancel_url='http://localhost:8000/cancel',
	)

	return JsonResponse({
		'session_id':session.id,
		'stripe_public_key':settings.STRIPE_PUBLISHABLE_KEY
	})


def success(request):
	context = {}
	template = loader.get_template('items/success.html')
	return HttpResponse(template.render(context, request))

def cancel(request):
	return HttpResponse('cancel')



@csrf_exempt
def my_web_hook_view(request):
	endpoint_secret = 'whsec_b11c2fc7fbc2499b28b69266525e50ac2399d9d988ce27250730736eaecb8a6f'
	payload = request.body
	event = None

	try:
		event = stripe.Event.construct_from(
			json.loads(payload), stripe.api_key
			)
	except ValueError as e:
    	# Invalid payload
		return HttpResponse(status=400)

  	# Handle the event
	if event.type == 'payment_intent.succeeded':
		payment_intent = event.data.object # contains a stripe.PaymentIntent
		# Then define and call a method to handle the successful payment intent.
		# handle_payment_intent_succeeded(payment_intent)
	elif event.type == 'payment_method.attached':
		payment_method = event.data.object # contains a stripe.PaymentMethod
		# Then define and call a method to handle the successful attachment of a PaymentMethod.
		# handle_payment_method_attached(payment_method)
  	
	# ... handle other event types
	else:
		print('Unhandled event type {}'.format(event.type))

	return HttpResponse(status=200)