import numpy as np
import cv2


class ImageProcessor:
    def __init__(self) -> None:
        pass

    @staticmethod
    def additive_noise(image, percent):
        places = np.random.rand(*image.shape)
        noise = np.random.normal(0, 5, image.shape) * (places < percent / 100)
        noisy_image = np.clip(image + noise, 0, 255)
        return noisy_image.astype(np.uint8)

    @staticmethod
    def mean_filter(image, kernel_size):
        return cv2.blur(image, (kernel_size, kernel_size))

    @staticmethod
    def gauss_filter(image, kernel_size):
        sigma = kernel_size // 2 / 3

        from scipy.ndimage import convolve

        def gauss(x, sigma):
            return 1 / np.sqrt(2 * np.pi * sigma ** 2) * \
                np.exp(- x ** 2 / (2 * sigma ** 2))

        r = kernel_size / 2
        kernel = np.zeros((kernel_size, 1))
        for i in range(kernel_size):
            kernel[i, 0] = gauss(i - r, sigma)

        return np.clip(convolve(convolve(image, kernel), kernel.T), 0, 255).astype(np.uint8)

    @staticmethod
    def image_equalization(image):
        hist, _ = np.histogram(image, bins=256, range=(0, 256))
        cdf = hist.cumsum()
        cdf_normalized = cdf / cdf[-1]

        equalized = np.interp(image.flatten(), np.arange(256), cdf_normalized * 255)
        return equalized.reshape(image.shape).astype(np.uint8)

    @staticmethod
    def statistic_correction(image, new_mean, new_std):
        image = image.astype(np.float32)
        mean, std = image.mean(), image.std()

        corrected_image = (image - mean) * (new_std / std) + new_mean
        corrected_image = np.clip(corrected_image, 0, 255).astype(np.uint8)

        return corrected_image

    @staticmethod
    def resize(image, new_width, new_height):
        return cv2.resize(image, (new_width, new_height))

    @staticmethod
    def shift(image, x, y):
        h, w = image.shape
        l, k = np.meshgrid(np.arange(h), np.arange(w), indexing='ij')

        x_new = (k - x) % w
        y_new = (l - y) % h

        return image[y_new, x_new]

    @staticmethod
    def rotation(image, k, l, angle):
        angle_rad = np.deg2rad(angle)

        height, width = image.shape[:2]
        x, y = np.meshgrid(np.arange(width), np.arange(height))

        x_new = (x - k) * np.cos(angle_rad) - (y - l) * np.sin(angle_rad) + k
        y_new = (x - k) * np.sin(angle_rad) + (y - l) * np.cos(angle_rad) + l

        rotated_image = np.zeros_like(image)
        x_new = np.clip(x_new, 0, width - 1).astype(int)
        y_new = np.clip(y_new, 0, height - 1).astype(int)

        rotated_image[y_new, x_new] = image[y, x]
        rotated_image[y_new, np.clip(x_new + 1, 0, width - 1)] = image[y, x]

        return rotated_image

    @staticmethod
    def glass_effect(image):
        height, width = image.shape[:2]
        x, y = np.meshgrid(np.arange(width), np.arange(height))

        rand_x = np.clip(x + np.random.randint(-5, 6, x.shape), 0, width - 1)
        rand_y = np.clip(y + np.random.randint(-5, 6, y.shape), 0, height - 1)

        return image[rand_y, rand_x]

    @staticmethod
    def waves(image):
        height, width = image.shape[:2]
        x, y = np.meshgrid(np.arange(width), np.arange(height))

        rand_x = np.clip(x + 20 * np.sin(2 * np.pi * y / 60), 0, width - 1).astype(int)

        return image[y, rand_x]

    @staticmethod
    def motion_blur(image, n):
        from scipy.ndimage import convolve
        I = np.eye(n) / n
        return convolve(image, I)
