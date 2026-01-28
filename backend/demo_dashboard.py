import streamlit as st
import pandas as pd
import numpy as np

# --- Page Configuration ---
st.set_page_config(layout="wide")
st.title("Live CO₂ Sequestration Calculation Dashboard")
st.markdown("This dashboard demonstrates how the raw measurements from drone imagery are converted into a final carbon sequestration value.")

# --- File Uploader ---
st.header("Step 1: Upload the Backend Output File")
st.write("After the backend finishes processing, it generates a `carbon_inventory.csv`. Please upload that file here to see the calculation breakdown.")
uploaded_file = st.file_uploader("Upload carbon_inventory.csv", type=['csv'])

if uploaded_file is not None:
    # Load the data
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File successfully loaded!")
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    # --- Display Raw Data ---
    st.header("Step 2: Review Raw Data from Drone Analysis")
    st.write(f"The backend successfully identified **{len(df)}** trees. Here are the direct measurements for a sample of them:")
    st.dataframe(df[['tree_id', 'height_m', 'crown_area_sqm']].head())

    # --- Explain the Calculation Steps ---
    st.header("Step 3: The Scientific Calculation Pipeline")
    st.write("We now apply a series of scientifically-validated formulas to this data.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("A. Aboveground Biomass (AGB)")
        st.markdown("We use **allometric equations**, which are like scientific recipes that convert tree dimensions (like height and estimated diameter) into biomass.")
        st.latex(r'''
        \text{AGB (kg)} = \alpha \cdot (\rho \cdot \text{DBH}^{ \beta })
        ''')
        st.write("Where `DBH` (trunk diameter) is estimated from height and crown area, and `ρ` (rho) is the wood density.")
        st.write("Resulting AGB for each tree:")
        st.dataframe(df[['tree_id', 'agb_kg']].head(), height=220)

    with col2:
        st.subheader("B. Total Biomass (including roots)")
        st.markdown("Mangrove roots store a significant amount of carbon. We estimate this **Belowground Biomass (BGB)** using a Root-to-Shoot ratio (e.g., 50% of AGB).")
        st.latex(r'''
        \text{Total Biomass} = \text{AGB} + \text{BGB}
        ''')
        st.write("Resulting Total Biomass for each tree:")
        st.dataframe(df[['tree_id', 'total_biomass_kg']].head(), height=220)

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("C. Carbon Content")
        st.markdown("On average, the dry biomass of a tree is about **47% carbon** by weight.")
        st.latex(r'''
        \text{Carbon (kg)} = \text{Total Biomass} \times 0.47
        ''')
        st.write("Resulting Carbon content for each tree:")
        st.dataframe(df[['tree_id', 'carbon_kg']].head(), height=220)

    with col4:
        st.subheader("D. CO₂ Sequestration")
        st.markdown("Finally, we convert the mass of carbon to the mass of carbon dioxide (CO₂) using their molecular weights (a ratio of **3.67**).")
        st.latex(r'''
        \text{CO}_2 \text{ (kg)} = \text{Carbon} \times 3.67
        ''')
        st.write("Final CO₂ sequestered per tree:")
        st.dataframe(df[['tree_id', 'co2_sequestered_kg']].head(), height=220)

    # --- Final Results ---
    st.header("Step 4: Final Aggregated Results")
    total_co2_tonnes = df['co2_sequestered_kg'].sum() / 1000

    st.metric(
        label="Total CO₂ Sequestered for this Plot",
        value=f"{total_co2_tonnes:,.2f} Tonnes"
    )
    st.info("Note: The final value is high due to the prototype's placeholder coefficients. In a real project, these would be scientifically calibrated.")

    # --- Visualization ---
    st.header("Visualization: CO₂ Contribution per Tree")
    st.write("This chart shows the CO₂ sequestered by the top 15 largest trees in the plot.")

    # Prepare data for charting
    chart_data = df.sort_values('co2_sequestered_kg', ascending=False).head(15)
    chart_data = chart_data.set_index('tree_id')

    st.bar_chart(chart_data['co2_sequestered_kg'])

else:
    st.info("Waiting for you to upload a `carbon_inventory.csv` file.")