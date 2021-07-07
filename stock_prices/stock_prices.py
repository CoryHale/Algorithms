# !/usr/bin/python

import argparse

def find_max_profit(prices):
	cur_min = 0
	cur_max = 1
	for i in range(2, len(prices) - 1):
		if prices[i] > prices[cur_max]:
			cur_max = i

	i = 1
	while i < cur_max:
		if prices[i] < prices[cur_min]:
			cur_min = i
			i += 1
		else:
			i += 1

	max_profit = prices[cur_max] - prices[cur_min]
	return max_profit
  


if __name__ == '__main__':
	# This is just some code to accept inputs from the command line
	parser = argparse.ArgumentParser(description='Find max profit from prices.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
	args = parser.parse_args()

	print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))