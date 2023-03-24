import streamlit as st
from PIL import Image
import base64
import numpy as np


image = Image.open('Images/page icon.png')
st.set_page_config(
    page_title="INTERVIEW SAGA",
    page_icon=image,
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://github.com/sharmakhushi9757',
        'Report a bug': "https://github.com/sharmakhushi9757",
        'About': "sharmakhushi9757"
    }
)


@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def build_markup_for_logo(
    png_file,
    background_position="10% 10%",
    margin_top="10%",
    image_width="30%",
    image_height="",
):
    binary_string = get_base64_of_bin_file(png_file)
    return """
            <style>
                [data-testid="stSidebarNav"] {
                    background-image: url("data:image/png;base64,%s");
                    background-repeat: no-repeat;
                    background-position: %s;
                    margin-top: %s;
                    background-size: %s %s;
                }
            </style>
            """ % (
        binary_string,
        background_position,
        margin_top,
        image_width,
        image_height,
    )


def add_logo(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(
        logo_markup,
        unsafe_allow_html=True,
    )

add_logo("Images/logo1.png")




st.header("Everything you need to crack your next interview")
st.subheader(":blue[Now!! All available at one place]")
st.sidebar.success("Select a page above.")
st.image("Images/backk.png")


cc1,cc2,cc3=st.columns(3)
with cc1:
    st.image("https://i.pinimg.com/564x/56/65/a1/5665a13e627cef12d66e88a2ed1cb019.jpg",caption="Practice Set")
with cc2:
    st.image("https://i.pinimg.com/564x/43/83/4c/43834c4236b7fd1d4e799f55ce32df9e.jpg",caption="Resume Building")
with cc3:
    st.image("https://i.pinimg.com/564x/c1/49/a0/c149a096cc84eb5972743be15b952f68.jpg",caption="Mock Interview")


st.write("**Our Users Have cracked interviews at :**")

cl1,cl2,cl3,c4=st.columns(4)
with cl1:
    st.image("https://i.pinimg.com/474x/f4/46/99/f44699e42fa39104aee1063aa2eb09f5.jpg")
with cl2:
    st.image("https://i.pinimg.com/474x/53/b0/e6/53b0e6c332aa9cb17300f14c2c053a95.jpg")
with cl3:
    st.image("https://i.pinimg.com/474x/cf/5b/81/cf5b81678e89560e7757aefccc50f629.jpg")
with cl4:
    st.image("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATYAAACjCAMAAAA3vsLfAAAAolBMVEX///8AfbYAuegAe7UAebQAc7EAdbIAd7MAcrEAcLD1+vwAtucAf7fi7vW61ebq8/jE2+rU5fDy+PuIt9Wqy+B1rM9Bk8GWv9ra6fJYnccrir2gxd2y0OM3jr/C2uljo8pwqs6As9OQvNhPmMQQr95UyO3m9/wSjcIak8URntAShbp2vd5yx+hoy+4SpdWL2PLE6vid3vSw5PbW8foywut60/H0b+6+AAAOfElEQVR4nO1caYPathaFkSwZD5vBrGanSVre60uatv//rz3de7XZ2MBMJ2nauedLM+BFOjp3lWinw2AwGAwGg8FgMBgMBoPBYDAYDAaDwWAwGAwGg8FgMBgMBoPBYDAYDAaDwWAwGAwGg8FgvDNkg9ffmheL06LI33A0/xjMe6vXzXtzTpTSBonaL994UD86sq3sinQ7fvGNRTeRXQshe7NvMLYfF7kQOO90+zLFDdZJtwK1/UYjfAO83gu1YJp6waSr0eP3DUlpQidpqkh0evXWg3sjlCpRm7d84HKtI73IpHx4JClqVOpjPsnyGQkvebmhfw8UPdEVvccFt1jPdzcvONLkA5L55LGRkEaTvb18g7zJ+cND+564wCTVw4o4JMZR33BYu77u1iH1I4oZ9/DiNAxlj3bayx4d2/eEBtr04sGrB6AIuW/7erRKr0hDLu4/f4ID6SZF+GiJckt+yCxkLV7iQHYwE9FmN6WSjayZF9zNJM54qzrGn2E8Vj9k2jvuSZk87D+WoCbdzIHJHkQLa2byrQolDFGmsppvbOF5vReE4u+IfH8+PX71SkmpGl38oh4KXsRbn0RZDU0r80RxeXxwPzBO51nT8k+26hZpQMmx4TaHAu+uyxho6w3fcvQ/GMb6ptQQ6Y3scE3xoLYg+17yeNb3ppgUi7+QL2abxeaR+L9oDqBViDorATmlaFd2nO8eS/nuYTAsy83diJwNS+skhonS6fy1mU+hlVbyPu2z5B5lCNlaYB4x2VN/rSAYTg/TJoueTC+pUoaHS9Vzjk+zWUVTl0RRSpr3QPy3E+1ydoqXNJ/O3LsXeHc3vZcBHB5jzfBStDwBA4IQd94Dozut1v31Pppsce5foGwZykSanEBfGfUpcQl4ZdlKobTUOukHpo2nIKou5HGSyKuc+pfKkwc9rfvR33OlezS7vGeNK45lw3l3XavEjo+y1krMoMVG69hcUi0FNJSm/jOoDVWGNSK+Iqk+xYUqCR08GU3TJ0s9n4pDvpNmrqqrTNwoQ6RxwgFuJYm0DWknze7iHhyzPlWiZmvlw6y1FnEbfVOLFoO18nEnJHMw12S37Pl3VCL2CDNmoZPztCyPB/85dhskxTFfK84FpUBrP3H3DWWVceU+NKshw+Ihbei7C59RiHX4emHe14sns3wkGnSNJPC/sa4DrGu77bM3lBcKaRyuDo4DCle5OAvotVCREjmVCbImZVnz7nvzQqFm5R6WXJ7tp7gCS5oRvsvXnDSJ2ByAHXkIfzvKOxe8krxboLnUtaR0fT/zMI/pf/r508U8TDV2T1Y03ZuRq8TlEUl3vyjK6da7Y6QcBqFm+XIGSx25chycWuGDB5uhu2kMz8Ki7QR3J5NAm5nqFOxtvo4IdVabhiAAF8U0IuVGbeME39ivVfrAclxcl/eyXHj7p5+eEL+0+C9coa66xdoGWdOXq1C5sA6fEryDjFf5AN/ZMnfcU94jIsvkL8BOXUUOw0jp235np8KQtlYakRsBkYtoMnBTagdgnBpmVNH6odoi2h6R2v+ePC6RVw6gFnqzARMG6MGbCo2SaBPUBR6hjqwHRZFI2x42nlraIiRPwdbp3yB0vQnDuHRG5i4TjydAW4oudIDXh5c4mmLa+nYCELGArTmOt4224f14ELP29NTowMg13yo+qU/jRD/VwditC3YKA2FYSS8hggiZeT7drGcy+KV9oG2SIBMb88CesUawM4oJRtCiuxIVg5A12gzl8HhQmRpankJIQWcQ0ba669mqrD390lRhkWBu0IauwFesm57Q3lyINm8PQAmFMAoHTnkwH2FTgEtkb6AKNfSXGJmZJ+ADYAGIUPMvtUGi/MxHsZDhZWYKIOaTtNxirzAY9bRKm7xHm/i5wtrTc1O3BdUmuq2sZbrSCjHSC97WNgHcAGGVBVjLhIKhsxNIGKwbAFV5IeC/SakgMzNRQ6oGJ7gXyCJeDwknKMTzgJ7Ph2CiEWgzDFsNwqJJ35qA1Qy0De7aaP+pRtt/GmiRlRleA8WWutIAnY/3ckSbL3fhTyGyzsBuOTpBIJ3kz3IVqIrYxKmpIgPywAVAiMbXmGtg/hB7fMqBgShq10IANV9mylMLMg4XnCu07e7FUflTjban/zbQQs229gQEvhc+ycZM068jhQQfToi2Tm47Mr7WwhBLjcJxcPZkidYALignTP/hS3BH6CVnGs14HJm5dU7BrWwojctDnjEN6+Se7WnbXO+33DRRo7ZfG2iZk9ra0t0N5gLBT8g4puG6h7wGVXUpEpuw+u4AxRSU2C7QBrFW2K4rWo4u4AF9twDovcytkLCRbdvHoX0EViiNO8DbXQGJ1KTOCISIA8Q92uom2kLbgfYR2vpxl4oZUvnntQemFbk6SuPAvuaBKOMdMe2jgWNGims0wqxtEd2pC+PSaBFA1PAaoAtl1Q9La51T6oe4ouzXTMQ5PIwJLiPECKJ8zjm8baS1KIq0fW7ghQxNt7R/bYrh/8b44JsClBj4Ec1oE0j0Shybcg00fAZdhnNG97WWUQymquho8g6ybGT3gv8ll3AOuUot67EBYAXM+hXUIviIXdVelrdDwuWKtafnLw3EoLeplL4x0CBC1KJ3KucISYrevmkDTBjjLCLPj2HR6TlTpE843mP4twXTjqYifdUA7wEzNDkFkQWGqKfuLZUNP1wJI80k+mwehVKs4YJJZDeN9DoeGNqaiMnqixeDLDiUzWSGqmJ9YVMIpiMUnAPYRAnnhPoNdvGBaXEeXYA16Ww/qq3paejLjBnOpSUfQxGuXtYzkojE1ClwTAIigh8KRGIXStFhRJX/uW1jFJ7ySwNrTTbqHtNopWOacXD61M9yZQIKFTIOO35wSBKtITYMarG4Tg8ZMhiR7DvW4tqaAmQGhmd8uhTW9WONJexbRBnX8jbrX3ej6Iq+ke7M6tZU3HBu1/HAoDnJoMcIff3tyGYSPgUakzE5xR/j/GM0x2hICYUznE7wJdZmfEWYnN0L4WLRt1cd7PrAFUtzryuiQMkpuIOtEHO8wzrcLPiqICksj8l7bKw1hem1lwmNJtrk2Tq2DGjat84utlMntP3EdiNcBkJtSFrHUlX2v6QrrgZ4STQn+0hf43YmJhCIdUmmU6m7NsYnuAJtZe3SGIBZNQysuX2xn7UO6cDalxVmzJg2hq5Za+NIgon+WmPtt2bWjGhoxEmtLzQxsU5si8hLQS8ZVUHB38oUpJidVXW96eSNOu9hTS7g6ojr3JqU9HEE3VyaU2Ty8QXL24sh1H2AOeGaErkBfb1ya+fUE/lnSHgxThsD0TPdrXTNLs1yE58wSfv49BxIe/7axlpnREIR1c2rMbRr0sEgNK/AvlS5dfV3FkqokTvq5BO8nLwiXtLLh9ZD7+bu9IBYWaPZYK5wJLMKtTGmRcCIS3bw3JDezyk5w8fjfsHeCHLRp6dG/Qi6IDdShj4MhujQ5lw2HvyQa6KqM/nw/GxJ+/CxlTUTH2mlRRJK/dEB3gub0ltKQXa7AyUFcDFU9hNrsVAN9m1wUqGlGuKVeSplr8MLDFdois5yOl7mJR5dwQ0SlLHXxNh5xENFIhgpYHXx5WpWgMr71nlUohpcLrqzLibQ+1o7eBh2Pzz0+suzs8rfP/9hJPfh8y3SYBBu2t1TPpqM8uKcYqcWgh9FU6lwr6A37ExAm/Kygr+R0Rk1crvVTb3MCTA92sAqUNRKFrTbJnSSJHRSbQ3Ko8LVeSebtUSew3WSSfm0sydhEL2xjU2VzVH0IEJSIMmdBgJvdb0l886fVmN3yIrm6N2DTNI0VXY7hVKGfcgPgYLOiXYIu7aGMmvslNGPg3G26im3FZq7XbykD266urerKE5DyhuF87Xd8wnPs0TaUvPg/Dp0nZGWWsZuDdcYtvkDdom6aXx8r185ASLTReejd2m/P8rbqHuVAwp/tPJsXYHbIbXuX/R2EEwMbSR5va4dfhgUixLd5YiyZpFsrXbK1L3OaM55BqisQjSfUn4XhXd0JcKf5rF7sLQ1CyaZVkOa3WnW6PBG1NePt/pPWlnnLHS6N2vxIUpwHxXcZK4qshXqEiR/MvIzwvEH9g+pljo1F+yJtjUcIEumzU/uDPZ0Bl3u8+gzBfvyKhFH3yUYG3UG4jEEVGuXVSqVDnnEIVVSWYvIezqpbzDt4A2pzQ5zY8+6GvOyYtVNkySV8wWM4c8QP00sePrjQeZK4Y9jCvOOysnVbDM9FdEMBuV0ARzsyUgni8OsbDma40ir990nw4V5ZuWoRn6skKSvcsnNtIjdgBmFf+tyer0/PrGjpCkU0/L6KNBkuaQnZB8i1gxvj7JmUMx1ogwSeb6zR++wku29ExrNDEmT167nLib9JP1evyfJfnuKWXt+as/WGm/Ph5vNcPnwISkbEloxlBge+8dKl+7RwWy+06HEry5PI/t8/uNlpL0c29u0HSC5lekJa/7Ws9p/O7LPQBbh6c+vj5vna7Gu7BDVMcc2yHxkGxI/6i+RAB+/fDX48u0ZQ0CfopW2uc+Ysf3WTu+7A+5qtZyMm+mQYRa1k1XvHEBbtM8bAwsD1x2ayvsn6N4RUG3Nrn4e77BAldB8TOxdAgvHxuMjeLwvdU21rejWfy3yngF0iMYzXgsd61CF00cMu/vRsAkRetiIQfKKbPdfDNyGavyhCG6huMoZA+kLflv2bwduZiRNP50QsTeD0rXxqncKbA/qpuMjIjrlg9sEt065vjtg4taUx65F4HMWDiIwEHCGvDHfnYVIij/HaP4Z7LvFtKdU0/+HgMz32OlkCzxjxAGhikGxKJqURAdWVD/Vr2hRvl+4PWvcReiziT6KpbBbavL1v6l9j8iOMlEqSeb/5h/cfxPk43HOSmMwGAwGg8FgMBgMBoPBYDAYDAaDwWAwGAwGg8FgMBgMBoPBYDAYDAaDwWAwGAwGg8Fg/GPwf6eLuDsRhC0sAAAAAElFTkSuQmCC")

 
    
