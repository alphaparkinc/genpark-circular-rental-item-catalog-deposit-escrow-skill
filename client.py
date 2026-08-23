class CircularRentalItemCatalogDepositEscrowClient:
    def rent_local_item(self, item_sku='RENT_SONY_A7IV_CAMERA', rental_duration_days=3, user_trust_tier='verified'):
        daily_rate = 35.0
        security_deposit = 250.0
        return {
            'rental_booking_id': 'omni_rnt_3341',
            'item_sku': item_sku,
            'rental_fee_usd': daily_rate * rental_duration_days,
            'security_deposit_escrow_usd': security_deposit,
            'smart_lock_pickup_code': 'LOCK_PIN_8912',
            'damage_protection_tier': 'COMPREHENSIVE_EQUIPMENT_SHIELD',
            'auto_refund_deposit_on_dropoff': True
        }
