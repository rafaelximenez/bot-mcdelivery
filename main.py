from engine import mcdonalds
import config

mc = mcdonalds.Mcdonalds(config)

is_active = mc.fill_delivery_data()
if is_active:
    mc.order_standard_snack()
    mc.check_out()