from extractors.deals import get_apart_deal

deals = get_apart_deal("26710")
for deal in deals:
    print(deal)
    print('----------------------')