import streamlit as st


def main():
    st.title("Find the maximum")
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    max_num = max(num1, num2, num3)

    st.subheader("Maximum Number:")
    st.write(max_num)
    

if __name__ =='__main__':
    main()
