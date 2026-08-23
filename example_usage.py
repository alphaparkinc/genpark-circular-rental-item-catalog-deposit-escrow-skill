from client import CircularRentalItemCatalogDepositEscrowClient

def main():
    client = CircularRentalItemCatalogDepositEscrowClient()
    res = client.rent_local_item('RENT_CAMPING_GEAR_SET', 4)
    print('Booking: ' + res['rental_booking_id'] + ' | Total Fee: $' + str(res['rental_fee_usd']))
    print('Deposit Escrow: $' + str(res['security_deposit_escrow_usd']) + ' (Auto-refund: ' + str(res['auto_refund_deposit_on_dropoff']) + ')')
    print('Smart Locker Pin: ' + res['smart_lock_pickup_code'])

if __name__ == '__main__':
    main()
