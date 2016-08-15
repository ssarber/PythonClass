
"""
Tests radio tower interaction and playback
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import pytest
import helpers
import params

# @pytest.mark.skipif(True, reason="notification test disabled")
def test_skipped_track(driver_load_global_map, screenshots_dir):
    print(__name__, ':TestNotifications.test_skipped_tracks()')

    driver = driver_load_global_map

    try:
        wait = WebDriverWait(driver, params.super_short_wait)

        helpers.execute_notification(driver, 'skippedTrack')
        helpers.wait_until_element_clickable(driver, "#%s" % params.notify_id)

        notify = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, params.notify_message_css)))
        ActionChains(driver).move_to_element(notify).perform()

        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-SkippedTrackWarning")
        notify.click()

        helpers.wait_until_element_offscreen(driver, "#%s" % params.notify_id)

    except:
        helpers.take_screenshot(
            driver, screenshots_dir, "TestNotifications-ERROR-SkippedTrackWarning")

        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="notification test disabled")

def test_no_radio_tracks(driver_load_global_map, screenshots_dir):
    print(__name__, ':TestNotifications.test_no_radio_tracks()')

    driver = driver_load_global_map

    try:
        wait = WebDriverWait(driver, params.super_short_wait)

        helpers.execute_notification(driver, 'noRadioTracks')

        helpers.wait_until_element_clickable(driver, "#%s" % params.notify_id)

        notify = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, params.notify_message_css)))

        ActionChains(driver).move_to_element(notify).perform()

        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-NoRadioTracksWarning")

        notify.click()

        helpers.wait_until_element_offscreen(driver, "#%s" % params.notify_id)

    except:
        helpers.take_screenshot(
            driver, screenshots_dir, "TestNotifications-ERROR-NoRadioTracksWarning")

        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="notification test disabled")
def test_available_media(driver_load_global_map, screenshots_dir):
    print(__name__, ':TestNotifications.test_available_media()')

    driver = driver_load_global_map

    try:
        wait = WebDriverWait(driver, params.super_short_wait)

        helpers.execute_notification(driver, 'availableMedia')

        helpers.wait_until_element_clickable(driver, "#%s" % params.notify_id)

        new_media_notification = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, params.notify_btn_one_css)))

        ActionChains(driver).move_to_element(new_media_notification).perform()

        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-NewMediaWarning")

        new_media_notification.click()

        helpers.wait_until_element_offscreen(driver, "#%s" % params.notify_id)

        # another notification ================================
        helpers.execute_notification(driver, 'availableMedia')

        helpers.wait_until_element_clickable(driver, "#%s" % params.notify_id)

        new_media_notification = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, params.notify_btn_one_css)))

        ActionChains(driver).move_to_element(new_media_notification).perform()

        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-NewMediaWarning2")

        new_media_notification.click()

        helpers.wait_until_element_offscreen(driver, "#%s" % params.notify_id)

    except:
        helpers.take_screenshot(
            driver, screenshots_dir, "TestNotifications-ERROR-NewMediaWarning")

        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="notification test disabled")
def test_radio_tower(driver_load_global_map, screenshots_dir):
    print(__name__, ':TestNotifications.test_touch_control()')

    driver = driver_load_global_map

    try:
        wait = WebDriverWait(driver, params.super_short_wait)

        helpers.execute_notification(driver, 'radioTowerOffScreen')

        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-RadioTowerOffscreen")

    except:
        helpers.take_screenshot(
            driver, screenshots_dir, "TestNotifications-ERROR-SkippedTrackWarning")

        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="notification test disabled")
def test_no_artist_tracks(driver_load_global_map, screenshots_dir):
    print(__name__, ':TestNotifications.test_no_artist_tracks()')

    driver = driver_load_global_map

    try:
        wait = WebDriverWait(driver, params.super_short_wait)
        helpers.execute_notification(driver, 'noArtistTracks')
        helpers.wait_until_element_clickable(driver, "#%s" % params.notify_content_id)

        notify = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, params.notify_message_css)))

        ActionChains(driver).move_to_element(notify).perform()
        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-BeforeClick")
        notify.click()
        helpers.wait_until_element_offscreen(driver, "#%s" % params.notify_id)
        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-AfterClick")

    except:
        helpers.take_screenshot(
            driver, screenshots_dir, "TestNotifications-ERROR")
        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="notification test disabled")
def test_no_album_tracks(driver_load_global_map, screenshots_dir):
    print(__name__, ':TestNotifications.test_no_album_tracks()')

    driver = driver_load_global_map

    try:
        wait = WebDriverWait(driver, params.super_short_wait)
        helpers.execute_notification(driver, 'noAlbumTracks')
        helpers.wait_until_element_clickable(driver, "#%s" % params.notify_content_id)
        notify = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, params.notify_message_css)))
        ActionChains(driver).move_to_element(notify).perform()
        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-BeforeClick")
        notify.click()
        helpers.wait_until_element_offscreen(driver, "#%s" % params.notify_id)
        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-AfterClick")

    except:
        helpers.take_screenshot(
            driver, screenshots_dir, "TestNotifications-ERROR")

        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="notification test disabled")
def test_collected_media(driver_load_global_map, screenshots_dir):
    print(__name__, ':TestNotifications.test_collected_media()')

    driver = driver_load_global_map

    try:
        wait = WebDriverWait(driver, params.super_short_wait)
        helpers.execute_notification(driver, 'collectedMedia')
        helpers.wait_until_element_clickable(driver, "#%s" % params.notify_content_id)
        helpers.wait_until_element_clickable(driver, "#%s" % params.notify_content_id)
        notify = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, params.notify_message_css)))
        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-BeforeClick")
        notify.click()
        helpers.wait_until_element_offscreen(driver, "#%s" % params.notify_id)
        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-AfterClick")

    except:
        helpers.take_screenshot(
            driver, screenshots_dir, "TestNotifications-ERROR")

        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="notification test disabled")
def test_invalid_move(driver_load_global_map, screenshots_dir):
    print(__name__, ':TestNotifications.test_invalid_move()')

    driver = driver_load_global_map

    try:
        wait = WebDriverWait(driver, params.super_short_wait)
        helpers.execute_notification(driver, 'invalidMove')
        helpers.wait_until_element_clickable(driver, "#%s" % params.notify_content_id)
        notify = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, params.notify_message_css)))
        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-BeforeClick")
        notify.click()
        helpers.wait_until_element_offscreen(driver, "#%s" % params.notify_id)
        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-AfterClick")

    except:
        helpers.take_screenshot(
            driver, screenshots_dir, "TestNotifications-ERROR")

        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="notification test disabled")
def test_missing_media_item(driver_load_global_map, screenshots_dir):
    print(__name__, ':TestNotifications.test_missing_media_item()')

    driver = driver_load_global_map

    try:
        wait = WebDriverWait(driver, params.super_short_wait)
        helpers.execute_notification(driver, 'missingMediaItem')
        helpers.wait_until_element_clickable(driver, "#%s" % params.notify_content_id)
        notify = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, params.notify_message_css)))
        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-BeforeClick")
        notify.click()
        helpers.wait_until_element_offscreen(driver, "#%s" % params.notify_id)
        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-AfterClick")

    except:
        helpers.take_screenshot(
            driver, screenshots_dir, "TestNotifications-ERROR")

        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="notification test disabled")
def test_invalid_subway_route(driver_load_global_map, screenshots_dir):
    print(__name__, ':TestNotifications.test_invalid_subway_route()')

    driver = driver_load_global_map

    try:
        wait = WebDriverWait(driver, params.super_short_wait)
        helpers.execute_notification(driver, 'invalidSubwayRoute')
        helpers.wait_until_element_clickable(driver, "#%s" % params.notify_content_id)
        helpers.wait_until_element_clickable(driver, "#%s" % params.notify_content_id)
        notify = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, params.notify_message_css)))
        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-BeforeClick")
        notify.click()
        helpers.wait_until_element_offscreen(driver, "#%s" % params.notify_id)
        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-AfterClick")

    except:
        helpers.take_screenshot(
            driver, screenshots_dir, "TestNotifications-ERROR")

        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="notification test disabled")
def test_invalid_playlist_number(driver_load_global_map, screenshots_dir):
    print(__name__, ':TestNotifications.test_invalid_playlist_number()')

    driver = driver_load_global_map

    try:
        wait = WebDriverWait(driver, params.super_short_wait)
        helpers.execute_notification(driver, 'invalidPlaylistNumber')
        helpers.wait_until_element_clickable(driver, "#%s" % params.notify_content_id)
        notify = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, params.notify_message_css)))
        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-BeforeClick")
        notify.click()
        helpers.wait_until_element_offscreen(driver, "#%s" % params.notify_id)
        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-AfterClick")

    except:
        helpers.take_screenshot(
            driver, screenshots_dir, "TestNotifications-ERROR")

        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="notification test disabled")
def test_touch_control(driver_load_global_map, screenshots_dir):
    print(__name__, ':TestNotifications.test_touch_control()')

    driver = driver_load_global_map

    try:
        wait = WebDriverWait(driver, params.super_short_wait)
        helpers.execute_notification(driver, 'touchControl')
        helpers.wait_until_element_clickable(driver, "#%s" % params.notify_content_id)

        # Firefox seems to like the CSS locator better
        notify = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, params.notify_message_css)))
        ActionChains(driver).move_to_element(notify).perform()
        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-TouchControlWarning")
        notify.click()
        wait.until(EC.element_to_be_clickable((By.ID, "toggle-pan")))
        helpers.take_screenshot(driver, screenshots_dir, "TestNotifications-STATUS-Controls")

    except:
        helpers.take_screenshot(
            driver, screenshots_dir, "TestNotifications-ERROR-SkippedTrackWarning")

        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)