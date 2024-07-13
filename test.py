from abc import ABC, abstractmethod
from dataclasses import dataclass
import numpy as np


class ValuationModel(ABC):
    @abstractmethod
    def calculate_intrinsic_value(self, **kwargs) -> float:
        pass

@dataclass
class DCFInputs:
    cash_flows: list
    projected_growth_rate: float
    discount_rate: float
    years_to_project: int
    perpetual_growth_rate: float
    cash_and_equivalents: float
    total_debt: float
    shares_outstanding: float


class DCFModel(ValuationModel):
    @staticmethod
    def calculate_average_growth_rate(cash_flows):
        growth_rates = [(cash_flows[i] / cash_flows[i - 1]) - 1 for i in range(1, len(cash_flows))]
        return np.mean(growth_rates)

    @staticmethod
    def project_future_cash_flows(initial_cash_flow, growth_rate, years):
        return [initial_cash_flow * (1 + growth_rate) ** i for i in range(1, years + 1)]

    @staticmethod
    def calculate_terminal_value(final_cash_flow, perpetual_growth_rate, discount_rate):
        return final_cash_flow * (1 + perpetual_growth_rate) / (discount_rate - perpetual_growth_rate)

    @staticmethod
    def calculate_present_values(cash_flows, discount_rate):
        return [cf / (1 + discount_rate) ** (i + 1) for i, cf in enumerate(cash_flows)]

    def calculate_intrinsic_value(self, **kwargs) -> float:
        inputs = DCFInputs(**kwargs)

        avg_growth_rate = self.calculate_average_growth_rate(inputs.cash_flows)
        print(f"Average Actual Growth Rate: {avg_growth_rate:.2%}")

        future_cash_flows = self.project_future_cash_flows(
            inputs.cash_flows[-1],
            inputs.projected_growth_rate,
            inputs.years_to_project
        )

        terminal_value = self.calculate_terminal_value(
            future_cash_flows[-1],
            inputs.perpetual_growth_rate,
            inputs.discount_rate
        )
        print(f"Future Terminal Value: {terminal_value:.2f}")

        present_values = self.calculate_present_values(future_cash_flows, inputs.discount_rate)
        print(f"Present Value of Future Free Cash Flow: {present_values}")

        present_terminal_value = terminal_value / (1 + inputs.discount_rate) ** (inputs.years_to_project + 1)
        print("Present Terminal Value: ", present_terminal_value)
        total_present_value = sum(present_values) + present_terminal_value
        equity_value = total_present_value + inputs.cash_and_equivalents - inputs.total_debt
        intrinsic_value = equity_value / inputs.shares_outstanding

        return intrinsic_value


@dataclass
class PEInputs:
    earnings: float
    pe_ratio: float
    shares_outstanding: float


class SimplePEModel(ValuationModel):
    def calculate_intrinsic_value(self, **kwargs) -> float:
        inputs = PEInputs(**kwargs)
        return (inputs.earnings * inputs.pe_ratio) / inputs.shares_outstanding


# Example usage
if __name__ == "__main__":
    # dcf_model = DCFModel()
    # dcf_intrinsic_value = dcf_model.calculate_intrinsic_value(
    #     cash_flows=[58896, 73365, 92953],
    #     projected_growth_rate=0.15,
    #     discount_rate=0.08,
    #     years_to_project=9,
    #     perpetual_growth_rate=0.025,
    #     cash_and_equivalents=62639,
    #     total_debt=124719,
    #     shares_outstanding=16070
    # )
    # print(f"DCF Intrinsic value per share: ${dcf_intrinsic_value:.2f}")
    #
    # pe_model = SimplePEModel()
    # pe_intrinsic_value = pe_model.calculate_intrinsic_value(
    #     earnings=92953,
    #     pe_ratio=15,
    #     shares_outstanding=16070
    # )
    # print(f"P/E Intrinsic value per share: ${pe_intrinsic_value:.2f}")

    cash_flows = [1000000, 1000000, 1000000, 1000000, 1000000]  # Example cash flows for 5 years

    discount_rate = 0.05  # 10% discount rate
    growth_rate = 0.00  # 2% perpetual growth rate

    dcf_model = DCFModel()
    dcf_intrinsic_value = dcf_model.calculate_intrinsic_value(
        cash_flows=cash_flows,
        projected_growth_rate=0.0,
        discount_rate=0.05,
        years_to_project=3,
        perpetual_growth_rate=0.00,
        cash_and_equivalents=0,
        total_debt=0,
        shares_outstanding=1
    )
    #$4329476
    print(dcf_intrinsic_value)
    # print(sum([952380.9523809523, 907029.4784580498, 863837.598531476, 822702.4747918819, 783526.1664684588]))