import sys
import math

args = sys.argv

if len(args) == 5:
	
	if args[1] == "--type=annuity":
		if 'principal' in args[2] and 'payment' in args[-2]:
			p = float(args[2][12:])
			payment = float(args[3][10:])
			i = float(args[4][11:])
			if p < 0 or payment < 0 or i < 0:
				print("Incorrect parameters")
			n_i = i/100 / 12 * 100 / 100
			x = payment
			y = payment - n_i * p
			z = x / y
			n = math.ceil(math.log(z, 1 + n_i))
			if n >= 12:
				years = 0
				months = 0
				if n % 12 == 0:
					years += int((n / 12))
					print('You need {} years to repay this credit!'.format(years))
					print('Overpayment = {}'.format(payment * n - p))
				else:
					years += int((n / 12))
					months += (n % 12)

					print('You need {} years and {} months to repay this credit!'.format(years, math.ceil(months)))
					print('Overpayment = {}'.format(payment * n - p))
			
			else:
				print('You need {} months to repay this credit!'.format(math.ceil(n)))
				print('Overpayment = {}'.format(payment * n - p))


		elif 'principal' in args[2]:
			p = float(args[2][12:])
			n = int(args[3][10:])
			i = float(args[4][11:])
			if p < 0 or n < 0 or i < 0:
				print("Incorrect parameters")
			n_i = i/100 / 12 * 100 / 100
			payment = math.ceil(p * ((n_i * (1 + n_i) ** n) / ((1 + n_i) ** n - 1)))
			print('Your annuity payment = {}!'.format(payment))
			print('Overpayment = {}'.format(int(payment * n - p)))

		elif 'payment' in args[2]:
			payment = float(args[2][10:])
			n = int(args[3][10:])
			i = float(args[4][11:])
			if payment < 0 or n < 0 or i < 0:
				print("Incorrect parameters")
			n_i = i/100 / 12 * 100 / 100
			x = payment
			y = n_i * math.pow(1 + n_i, n)
			z = math.pow(1 + n_i, n) - 1
			principal = int(x / (y / z))

			print('Your credit principal = {}!'.format(principal))
			print('Overpayment = {}'.format(int(payment * n - principal)))


	elif args[1] == "--type=diff":
		if len(args[2]) <= 12 or len(args[3]) <= 10 or len(args[4]) <= 11:
			print("Incorrect parameters")
		else:
			p = float((args[2][12:]))
			n = int(args[3][10:])
			i = float(args[4][11:])
			if p < 0 or n < 0 or i < 0:
				print("Incorrect parameters")
			n_i = i/100 / 12 * 100 / 100
			total = 0
			for m in range(1,n+1):
				diff_payment = math.ceil((p/n) + n_i * (p - (p * (m - 1)) / n))
				total += diff_payment
				print('Month {}: paid out {}'.format(m,diff_payment))
			print('\n')
			print('Overpayment = {}'.format(int(total - p)))

	else:
		print("Incorrect parameters")

else:
	print("Incorrect parameters")
