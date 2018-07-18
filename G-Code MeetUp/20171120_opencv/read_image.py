import cv2
import numpy as np

if __name__=='__main__':
    image=cv2.imread('./images/Lenna.png')
    # cv2.imshow('read_result',image)
    print('Shapte of image: ', image.shape)

    # 각각의 bgr 값을 1채널(그래이스케일)로 변환
    b,g,r=cv2.split(image)
    # 반대는 merge

    cv2.imshow('b',b)
    cv2.imshow('g',g)
    cv2.imshow('r',r)

    filter=np.array([[1,0,-1],
                     [1,0,-1],
                     [1,0,-1]])

    filtered_b = cv2.filter2D(src=b,kernel=filter, ddepth=-1)
    filtered_g = cv2.filter2D(src=g,kernel=filter, ddepth=-1)
    filtered_r = cv2.filter2D(src=r,kernel=filter, ddepth=-1)

    # cv2.imshow('filtered_b',filtered_b)
    # cv2.imshow('filtered_g',filtered_g)
    # cv2.imshow('filtered_r',filtered_r)

    concentration = filtered_b+filtered_g+filtered_r
    cv2.imshow('concentration',concentration)

    filtered=cv2.merge((filtered_b, filtered_g, filtered_r))
    cv2.imshow('filter',filtered)

    cv2.waitKey(0)