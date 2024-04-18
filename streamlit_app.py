import streamlit as st

st.markdown("""<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous"> """, unsafe_allow_html=True)
st.markdown(""" <nav class="navbar bg-primary sticky-top">
        <div class="container-fluid">
         <p>
         App by Vijay
        </p>
        </div>
      </nav> """, unsafe_allow_html=True)
def find_largest(a, b, c):
    return max(a, b, c)

left_column, right_column = st.columns(2)

with right_column:
    number1 = st.number_input("Enter the first number:")
    number2 = st.number_input("Enter the second number:")
    number3 = st.number_input("Enter the third number:")
    if st.button("Find Largest"):
        largest = find_largest(number1, number2, number3)
        st.markdown(f""" <div class="alert alert-success" role="alert">
                <small class="text-body-secondary">The largest number is : <h1> {largest} </h1> </small>
                </div>""", unsafe_allow_html=True)

with left_column:
    st.title("Find the Largest Number")
    st.write('Harnessing the power of sophisticated artificial intelligence, I have developed an algorithm that stands unrivaled across the globe. Its sole purpose? To determine the largest among three input numbers you provide.')

st.markdown(f"""<div class="bg-dark text-secondary px-4 py-5 text-center">
          <div class="py-5">
            <h1 class="display-5 fw-bold text-white">Find the largest of 3 Numbers.</h1>
            <div class="col-lg-6 mx-auto">
              <p class="fs-5 mb-4">@copyright vijay 22f2001675 y-2024.</p>
            </div>
          </div>
        </div> """, unsafe_allow_html=True)