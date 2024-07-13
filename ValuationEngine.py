import numpy as np


def discounted_cash_flow_analysis(cash_flows, discount_rate, growth_rate=0.0):
    """
    Perform Discounted Cash Flow (DCF) analysis.

    Parameters:
    cash_flows (list): List of future cash flows.
    discount_rate (float): Discount rate (as a decimal, e.g., 0.1 for 10%).
    growth_rate (float): Perpetual growth rate for terminal value (as a decimal, e.g., 0.02 for 2%).

    Returns:
    tuple: (NPV, NPV with terminal value)
    """




    def present_value(future_value, discount_rate, period):
        return future_value / (1 + discount_rate) ** period

    def net_present_value(cash_flows, discount_rate):
        npv = 0
        for i, cash_flow in enumerate(cash_flows):
            npv += present_value(cash_flow, discount_rate, i + 1)
        return npv

    def terminal_value(last_cash_flow, discount_rate, growth_rate):
        return last_cash_flow * (1 + growth_rate) / (discount_rate - growth_rate)

    # Calculate NPV of the cash flows
    npv = net_present_value(cash_flows, discount_rate)

    # Calculate terminal value if a growth rate is provided
    if growth_rate > 0:
        tv = terminal_value(cash_flows[-1], discount_rate, growth_rate)
        npv_with_tv = npv + present_value(tv, discount_rate, len(cash_flows))
    else:
        npv_with_tv = npv

    return npv, npv_with_tv


# Example usage
# cash_flows = [1000000, 1000000, 4000000, 4000000, 6000000]  # Example cash flows for 5 years
# discount_rate = 0.05  # 10% discount rate
# growth_rate = 0.02  # 2% perpetual growth rate


cash_flows = [1000000, 1000000, 1000000, 1000000, 1000000]  # Example cash flows for 5 years
discount_rate = 0.05  # 10% discount rate
growth_rate = 0.00  # 2% perpetual growth rate

npv, npv_with_tv = discounted_cash_flow_analysis(cash_flows, discount_rate, growth_rate)

print(f"The Net Present Value (NPV) of the cash flows is: ${npv:.2f}")
print(f"The Net Present Value (NPV) with terminal value is: ${npv_with_tv:.2f}")
