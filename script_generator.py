
import streamlit as st

investment_options = {
    "Liquidity and money market funds": 1,
    "Bonds": 2,
    "Equities": 3,
    "Multi-asset funds": 4,
    "Hedge funds": 5,
    "Private markets": 6,
    "Real estate": 7,
    "Precious metals and commodities": 8,
    "Structured products": 9,
    "Derivatives": 10
}

detailed_knowledge = {
    1: "The client understands the characteristics of liquidity and money market funds, recognizing their role in capital preservation and short-term cash management.",
    2: "The client understands fixed income strategies, including duration risk, credit quality, and interest rate sensitivity.",
    3: "The client has knowledge of equity markets, including volatility, sector diversification, and long-term capital appreciation.",
    4: "The client is familiar with multi-asset fund structures and the principles of portfolio diversification through strategic asset allocation.",
    5: "The client is aware of hedge fund strategies and understands the associated leverage, liquidity constraints, and performance dispersion.",
    6: "The client understands private market investments, including private equity and venture capital, and the associated illiquidity and time horizon.",
    7: "The client is familiar with real estate investments, including direct and indirect exposure, valuation risks, and income-generating potential.",
    8: "The client understands the role of commodities and precious metals in portfolio diversification and inflation protection.",
    9: "The client has knowledge of structured products, including principal protection features, contingent payoffs, and counterparty risk.",
    10: "The client understands derivative instruments such as options and futures and their application in risk management and tactical positioning."
}

detailed_experience = {
    1: "The client has invested in money market funds for liquidity management and preservation of capital in volatile markets.",
    2: "The client has actively allocated to bond portfolios across different maturities and credit segments to meet income and diversification goals.",
    3: "The client has invested in equity funds and individual stocks, demonstrating familiarity with public markets and long-term capital growth strategies.",
    4: "The client has experience investing in multi-asset solutions, using them to implement diversified strategies across equities, fixed income, and alternatives.",
    5: "The client has experience with hedge fund allocations, including long/short equity, macro, and event-driven strategies, appreciating their role in absolute return generation.",
    6: "The client has committed capital to private equity and venture capital funds, understanding the long-term nature, illiquidity, and return potential of private market investments.",
    7: "The client has invested in real estate through direct ownership or vehicles such as REITs and private property funds, recognizing its role in income generation and inflation hedging.",
    8: "The client has allocated to commodities and precious metals, such as gold and energy, as part of a diversified portfolio and inflation-sensitive exposure.",
    9: "The client has structured product experience, having invested in yield-enhancing and capital-protected instruments tailored to specific market views.",
    10: "The client has utilized derivatives for hedging and tactical exposure, including options, futures, and swaps across equity and fixed income markets."
}

def format_list(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return " and ".join(items)
    else:
        return ", ".join(items[:-1]) + ", and " + items[-1]

st.set_page_config(page_title="Client Script Generator", layout="centered")
st.title("Client Knowledge & Experience Generator")

selected_assets = {}
for label, idx in investment_options.items():
    level = st.selectbox(
        f"{label}:", ["None", "Knowledge only", "Knowledge and experience"],
        key=label
    )
    if level != "None":
        selected_assets[idx] = 1 if level == "Knowledge only" else 2

if st.button("Generate Summary & Paragraph"):
    knowledge_only_ids = [i for i, l in selected_assets.items() if l == 1]
    knowledge_exp_ids = [i for i, l in selected_assets.items() if l == 2]

    ko_names = [name for name, idx in investment_options.items() if idx in knowledge_only_ids]
    ke_names = [name for name, idx in investment_options.items() if idx in knowledge_exp_ids]

    summary_parts = []
    if ko_names:
        summary_parts.append(f"The client has knowledge in {format_list(ko_names)}")
    if ke_names:
        summary_parts.append(f"has knowledge and experience in {format_list(ke_names)}")
    summary_sentence = " and ".join(summary_parts) + "."

    detailed_parts = []
    for i in knowledge_only_ids:
        detailed_parts.append(detailed_knowledge[i])
    for i in knowledge_exp_ids:
        detailed_parts.append(detailed_experience[i])
    detailed_paragraph = " ".join(detailed_parts)

    st.subheader("📝 Summary")
    st.write(summary_sentence)
    st.subheader("📄 Detailed Paragraph")
    st.write(detailed_paragraph)
