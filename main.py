from engine import mcdonalds
import config

mc = mcdonalds.Mcdonalds(config)
mc.fill_delivery_data()
mc.order_standard_snack()
mc.check_out()