import frappe
from frappe.www.login import get_context as get_login_context

no_cache = True


def get_context(context):
	context = get_login_context(context) or context

	# `context.logo` comes from get_app_logo(), which always falls back to the
	# Frappe/ERPNext logo. The co-brand next to the Reflection mark should only
	# appear when an App Logo is actually attached in Website Settings.
	context.app_logo = frappe.db.get_single_value("Website Settings", "app_logo")

	return context
