import streamlit as st
import pickle
import pandas as pd
import time

st.set_page_config(
    page_title="Customer Churn Intelligence",
    page_icon="📊",
    layout="wide"
)

with open("customer_churn_model.pkl", "rb") as file:
    model = pickle.load(file)

st.markdown("""
<style>
    .main {
        background-color: #f5f7fb;
    }

    .title {
        font-size: 42px;
        font-weight: 700;
        color: #1f2937;
    }

    .subtitle {
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 30px;
    }

    .card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        text-align: center;
    }

    .card-title {
        font-size: 15px;
        color: #6b7280;
    }

    .card-value {
        font-size: 30px;
        font-weight: 700;
        color: #111827;
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📊 Churn Intelligence")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Dashboard", "🔍 Analyze Customer"]
)

if page == "🏠 Dashboard":

    st.markdown(
        '<div class="title">Customer Churn Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'AI-powered customer churn analysis and prediction dashboard'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-title">Total Customers</div>
            <div class="card-value">7,043</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">Churn Rate</div>
            <div class="card-value">26.5%</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-title">High Risk Customers</div>
            <div class="card-value">842</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <div class="card-title">Model Accuracy</div>
            <div class="card-value">80.62%</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("📊 Customer Risk Overview")

    risk_data = pd.DataFrame({
        "Risk Level": ["Low Risk", "Medium Risk", "High Risk"],
        "Customers": [4200, 2001, 842]
    })

    st.bar_chart(
        risk_data,
        x="Risk Level",
        y="Customers"
    )

    st.markdown("---")

    st.subheader("🤖 Model Performance")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Best Model", "Logistic Regression")

    with col2:
        st.metric("Accuracy", "80.62%")

    st.markdown("---")

    st.info(
        "💡 Use the **Analyze Customer** page from the sidebar "
        "to evaluate an individual customer's churn risk."
    )

else:

    st.title("🔍 Analyze Customer")
    st.write("Enter the customer's key details to predict churn risk.")

    left, right = st.columns(2)

    with left:

        st.subheader("👤 Customer Details")

        tenure = st.number_input(
            "Tenure (months)",
            min_value=0,
            max_value=100,
            value=12
        )

        monthly_charges = st.number_input(
            "Monthly Charges",
            min_value=18.25,
            max_value=118.75,
            value=70.0,
            step=1.0
        )

        total_charges = tenure * monthly_charges

        st.info(
            f"💰 Total Charges (Auto): ${total_charges:.2f}"
        )

        contract = st.selectbox(
            "Contract Type",
            ["Month-to-month", "One year", "Two year"]
        )

        internet_service = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"]
        )

        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer",
                "Credit card"
            ]
        )

        complaints = st.number_input(
            "Complaints",
            min_value=0,
            max_value=20,
            value=0
        )

        st.caption(
            "Complaints is shown for customer context and is not "
            "used by the trained model."
        )

        analyze = st.button(
            "🔎 ANALYZE CUSTOMER",
            use_container_width=True
        )

    with right:

        st.subheader("🎯 Prediction Result")

        if analyze:

            with st.spinner("Analyzing customer risk..."):
                time.sleep(1)

                input_data = {
                    feature: 0
                    for feature in model.feature_names_in_
                }

                input_data["SeniorCitizen"] = 0
                input_data["tenure"] = tenure
                input_data["MonthlyCharges"] = monthly_charges
                input_data["TotalCharges"] = total_charges

                if contract == "One year":
                    input_data["Contract_One year"] = 1

                elif contract == "Two year":
                    input_data["Contract_Two year"] = 1

                if internet_service == "Fiber optic":
                    input_data["InternetService_Fiber optic"] = 1

                elif internet_service == "No":
                    input_data["InternetService_No"] = 1

                if payment_method == "Credit card":
                    input_data[
                        "PaymentMethod_Credit card (automatic)"
                    ] = 1

                elif payment_method == "Electronic check":
                    input_data[
                        "PaymentMethod_Electronic check"
                    ] = 1

                elif payment_method == "Mailed check":
                    input_data[
                        "PaymentMethod_Mailed check"
                    ] = 1

                input_df = pd.DataFrame([input_data])

                input_df = input_df[
                    model.feature_names_in_
                ]

                prediction = model.predict(input_df)[0]

                probability = model.predict_proba(
                    input_df
                )[0][1]

                probability_percent = round(
                    probability * 100
                )

            if probability >= 0.70:
                risk = "HIGH 🔴"

            elif probability >= 0.40:
                risk = "MEDIUM 🟠"

            else:
                risk = "LOW 🟢"

            st.metric(
                "Churn Risk",
                risk
            )

            st.metric(
                "Probability",
                f"{probability_percent}%"
            )

            st.progress(probability)

            st.markdown("---")

            st.subheader("⚠️ Risk Factors & Customer Context")

            reasons = []

            if tenure < 12:
                reasons.append("Shorter customer tenure")

            if monthly_charges > 70:
                reasons.append("Higher monthly charges")

            if contract == "Month-to-month":
                reasons.append("Month-to-month contract")

            if internet_service == "Fiber optic":
                reasons.append("Fiber optic internet service")

            if payment_method == "Electronic check":
                reasons.append("Electronic check payment method")

            if not reasons:
                reasons.append(
                    "No major risk factors identified from the selected details."
                )

            for reason in reasons:
                st.write("• " + reason)

            st.subheader("🔑 Key Factors")

            if contract == "Month-to-month":
                st.write("📌 Contract type")

            if monthly_charges > 70:
                st.write("📌 Monthly charges")

            if tenure < 12:
                st.write("📌 Customer tenure")

            if payment_method == "Electronic check":
                st.write("📌 Payment method")

            if not any([
                contract == "Month-to-month",
                monthly_charges > 70,
                tenure < 12,
                payment_method == "Electronic check"
            ]):
                st.write("📌 Overall customer profile")

            st.subheader("💡 Recommended Action")

            if probability >= 0.70:

                st.error(
                    "High churn risk. Offer a personalized retention "
                    "plan, discount, or long-term contract."
                )

            elif probability >= 0.40:

                st.warning(
                    "Moderate churn risk. Provide a personalized "
                    "retention offer and monitor engagement."
                )

            else:

                st.success(
                    "Customer appears relatively stable. Continue "
                    "regular engagement and service support."
                )