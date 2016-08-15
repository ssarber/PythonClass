"""
Searches for a single artist and compares the result and expected number of results.
"""
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException

import pytest
import helpers
import params
import sidebar_helpers
from .browserop import map
from .browserop.eventlistener import function_triggers_event
from .screenshot import screenshot_on_error, take_screenshot
import video_helpers


username = params.username_default
password = params.password


@pytest.yield_fixture
def driver_load_personal_map_with_memory_stats(driver_load_personal_map):
    """
    Fixture that yields a webdriver for a loaded personal map that
    prints out Javascript heap snapshots on entry.
    """

    driver = driver_load_personal_map

    # print_js_heap_data() only works in Chrome
    if helpers.is_browser_chrome(driver):
        helpers.print_js_heap_data(driver)

    yield driver

    if helpers.is_browser_chrome(driver):
        helpers.print_js_heap_data(driver)


# @pytest.mark.skipif(True, reason="Disabled since add album is no longer valid, need to rewrite with artist pick.")
def test_pick_artist_sidebar(driver_load_personal_map_with_memory_stats, screenshots_dir):
    print(__name__, ':TestPersonalMapCreation.test_pick_artist_sidebar()')

    driver = driver_load_personal_map_with_memory_stats

    try:
        wait = WebDriverWait(driver, params.wait_time)

        map.wait_personal_ready(driver)

        helpers.wait_until_batch_save_complete(driver)

        helpers.clear_personal_media_direct(driver)

        map.wait_global_ready(driver)

        before_add_num = helpers.get_number_of_items_in_picklist(driver)
        take_screenshot( driver, screenshots_dir,
             "TestPersonalMapCreation-BeforeAddingArtist %s picks" % before_add_num)

        sidebar_helpers.pick_artist_sidebar(
            driver,
            screenshots_dir,
            "Pick artist via sidebar: %s" % params.personal_artists[0],
            params.personal_artists[0]
        )

        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-AfterAdding %s" % params.personal_artists[0])

        sleep(5)

        helpers.print_timestamped_message(driver, "7")

        wait.until(EC.text_to_be_present_in_element((By.ID, "new-pick-count"), "1"))

        helpers.print_timestamped_message(driver, "7.5")

        countElement = driver.find_element_by_id("new-pick-count")
        after_add_num = countElement.text

        helpers.print_timestamped_message(driver, "8")

        assert after_add_num > before_add_num

    except TimeoutException:
        take_screenshot(
            driver, screenshots_dir, "TestPersonalMapCreation-ERROR-TimeoutError")
        raise
    except UnexpectedAlertPresentException:
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-ERROR-UnexpectedAlertPresentException")
        alert = driver.switch_to_alert()
        alert.send_keys('8080')
        alert.dismiss()
    except:
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-ERROR-UncaughtException")
        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="Disabled since add album is no longer valid, need to rewrite with artist pick.")
def test_pick_artist_map(driver_load_personal_map_with_memory_stats, screenshots_dir):
    print(__name__, ':TestPersonalMapCreation.test_pick_artist_map()')

    driver = driver_load_personal_map_with_memory_stats

    try:
        wait = WebDriverWait(driver, params.wait_time)

        before_add_num = helpers.get_number_of_items_in_picklist(driver)
        take_screenshot( driver, screenshots_dir,
             "TestPersonalMapCreation-BeforeAddingArtist %s picks" % before_add_num)

        sidebar_helpers.pick_artist_map(
            driver,
            screenshots_dir,
            "Pick artist via map",
            params.personal_artists[1]
        )

        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-AfterAdding %s" % params.personal_artists[1])

        wait.until(EC.text_to_be_present_in_element((By.ID, "new-pick-count"), "2"))
        countElement = driver.find_element_by_id("new-pick-count")
        after_add_num = countElement.text

        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-AfterAddingAlbum %s picks" % after_add_num)

        assert after_add_num > before_add_num,\
            "TestPersonalMapCreation-ERROR-InvalidComparison"

    except TimeoutException:
        take_screenshot(
            driver, screenshots_dir, "TestPersonalMapCreation-ERROR-TimeoutError")
        raise
    except UnexpectedAlertPresentException:
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-ERROR-UnexpectedAlertPresentException")
        alert = driver.switch_to_alert()
        alert.send_keys('8080')
        alert.dismiss()
    except:
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-ERROR-UncaughtException")
        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="Disabled since add album is no longer valid, need to rewrite with artist pick.")
def test_create_map(driver_load_personal_map_with_memory_stats, screenshots_dir):
    print(__name__, ':TestPersonalMapCreation.test_create_map()')

    driver = driver_load_personal_map_with_memory_stats

    try:
        wait = WebDriverWait(driver, params.wait_reset)

        sidebar_helpers.open_add_sidebar(driver)

        arrange_button = wait.until(EC.element_to_be_clickable((By.ID, "collection-new-map-btn")))

        take_screenshot( driver, screenshots_dir,
             "TestPersonalMapCreation-CollectionTabOpen")

        arrange_button.click()

        helpers.wait_until_is_edit_mode(driver)

        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-AfterAdding %s" % params.personal_artists[1])

        helpers.wait_until_batch_save_complete(driver)

        take_screenshot( driver, screenshots_dir,
             "TestPersonalMapCreation-MapCreated")

        artist_count = helpers.get_media_node_count(driver)

        assert artist_count == 2, "TestPersonalMapCreation-WrongArtistCount %s" % artist_count
    except TimeoutException:
        take_screenshot(
            driver, screenshots_dir, "TestPersonalMapCreation-ERROR-TimeoutError")
        raise
    except UnexpectedAlertPresentException:
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-ERROR-UnexpectedAlertPresentException")
        alert = driver.switch_to_alert()
        alert.send_keys('8080')
        alert.dismiss()
    except:
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-ERROR-UncaughtException")
        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="Disabled since add album is no longer valid, need to rewrite with artist pick.")
def test_verify_map(driver_load_personal_map_with_memory_stats, screenshots_dir):
    print(__name__, ':TestPersonalMapCreation.test_verify_map()')

    driver = driver_load_personal_map_with_memory_stats

    try:
        wait = WebDriverWait(driver, params.long_wait)

        helpers.wait_until_batch_save_complete(driver)

        helpers.take_screenshot(
            driver, screenshots_dir, "TestPersonalMapCreation-MapBeforeRefresh")

        positions1 = helpers.get_node_positions(driver)

        helpers.print_timestamped_message(driver, "Trying to refresh page")

        driver.get(driver.current_url)

        helpers.print_timestamped_message(driver, "Waiting for ready")

        map.wait_personal_ready(driver)

        helpers.print_timestamped_message(driver, "Ready")

        positions2 = helpers.get_node_positions(driver)

        helpers.take_screenshot(
            driver, screenshots_dir, "TestPersonalMapCreation-MapAfterRefresh")

        helpers.assert_list_almost_equal(positions1, positions2, params.position_precision, "TestPersonalMapCreation-ERROR")

    except TimeoutException:
        take_screenshot(
            driver, screenshots_dir, "TestPersonalMapCreation-ERROR-TimeoutError")
        raise
    except UnexpectedAlertPresentException:
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-ERROR-UnexpectedAlertPresentException")
        alert = driver.switch_to_alert()
        alert.send_keys('8080')
        alert.dismiss()
        raise
    except:
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-ERROR-UncaughtException")
        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="Disabled since add album is no longer valid, need to rewrite with artist pick.")
def test_add_another_artist(driver_load_personal_map_with_memory_stats, screenshots_dir):
    print(__name__, ':TestPersonalMapCreation.test_add_another_artist()')

    driver = driver_load_personal_map_with_memory_stats

    try:
        wait = WebDriverWait(driver, params.long_wait)

        before_add_num = helpers.get_number_of_items_in_picklist(driver)
        take_screenshot( driver, screenshots_dir,
             "TestPersonalMapCreation-BeforeAddingArtist %s picks" % before_add_num)

        sidebar_helpers.pick_artist_search(
            driver,
            screenshots_dir,
            "Picked artist via search",
            params.personal_artists[2]
        )

        sidebar_helpers.open_sidebar(driver)
        sidebar_helpers.open_add_sidebar(driver)

        wait.until(EC.text_to_be_present_in_element(
            params.COLLECTION_ICON_ITEM_COUNT, "1"))

        add_to_map_button = helpers.wait_until_element_clickable(
            driver, params.ADD_TO_MAP_BTN)

        # sleep(2)
        helpers.move_to(add_to_map_button, driver)

        add_to_map_button.click()

        # first, wait till were in edit mode
        helpers.wait_until_is_edit_mode(driver)

        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-AfterAdding %s" % params.personal_artists[2])

        # then wait till we're out of it
        helpers.wait_until_batch_save_complete(driver)

        artist_count = helpers.get_media_node_count(driver)

        assert artist_count == 3, "TestPersonalMapCreation-WrongArtistCount %s" % artist_count

        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-MapSavedAfterAdding %s" % params.personal_artists[2])

    except TimeoutException:
        take_screenshot(
            driver, screenshots_dir, "TestPersonalMapCreation-ERROR-TimeoutError")
        raise
    except UnexpectedAlertPresentException:
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-ERROR-UnexpectedAlertPresentException")
        alert = driver.switch_to_alert()
        alert.send_keys('8080')
        alert.dismiss()
    except:
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-ERROR-UncaughtException")
        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# does clicking on a media cube open the info panel
# @pytest.mark.skipif(True, reason="Disabled for development")
def test_media_interaction(driver_load_personal_map_with_memory_stats, screenshots_dir):
    print(__name__, ':TestPersonalMapCreation.test_open_info_panel()')

    driver = driver_load_personal_map_with_memory_stats

    try:

        wait = WebDriverWait(driver, params.wait_time)

        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-MapBeforeClicking")

        zoom_to_media = lambda: helpers.zoom_to_media(driver, params.personal_artist_core_id)

        # make sure we zoomed
        wait.until(function_triggers_event(driver, zoom_to_media, 'zoomedToLocation'))

        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-AfterZoom")

        helpers.tap_media(driver, params.personal_artist_core_id)

        # make sure the media info tab opened up
        wait.until(EC.element_to_be_clickable((By.ID, "mediabar")))

        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-InfoTabOpen")

        # second tap should play
        helpers.tap_media(driver, params.personal_artist_core_id)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='close icon-x']")))

        video_helpers.check_video_duration(driver, screenshots_dir)

        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-VideoPlaying")

    except:
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-ERROR-FailedToOpenInfo")
        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# does another video play when the first one finishes
# @pytest.mark.skipif(True, reason="Disabled for development")
def test_video_autoplay(driver_load_personal_map_with_memory_stats, screenshots_dir):
    print(__name__, ':TestPersonalMapCreation.test_video_autoplay()')

    driver = driver_load_personal_map_with_memory_stats

    try:

        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-FirstVideo")

        first_duration = video_helpers.check_video_duration(driver, screenshots_dir)

        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-FirstVideoPlaying Duration %s" % first_duration)

        driver.execute_script("mg.event.bus.trigger('skipTrack')")

        sleep(5)

        second_duration = video_helpers.check_video_duration(driver, screenshots_dir)

        assert int(second_duration) != int(first_duration), "Duration of second song should be different from first"
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-SecondVideoPlaying Duration %s" % second_duration)
    except:
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-ERROR-FailedToPlayVideo")
        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="Disabled for development")
def test_auto_arrange_layout(driver_load_personal_map_with_memory_stats, screenshots_dir):
    print(__name__, ':TestPersonalMapCreation.test_auto_arrange_layout()')

    driver = driver_load_personal_map_with_memory_stats

    take_screenshot(driver, screenshots_dir, "TestPersonalMapCreation-MapBeforeResetLayout")
    sleep(1)

    try:
        wait = WebDriverWait(driver, params.short_wait)
        before_arrange_labels = helpers.get_label_positions(driver)
        assert before_arrange_labels is not None, "Invalid response for a label list"
        before_label = before_arrange_labels.pop()

        helpers.open_settings_menu(driver)

        auto_arrange_button = wait.until(EC.element_to_be_clickable((By.ID, "reset-layout-link")))
        auto_arrange_button.click()
        sleep(3)

        try:
            # at this point the page should refresh.
            modal_yes = wait.until(EC.element_to_be_clickable((By.ID, "modal-yes-button")))
            modal_yes.click()
            sleep(2)
        except TimeoutException:
            helpers.print_timestamped_message(driver, "Modal window could not be clicked")
            take_screenshot(driver, screenshots_dir,
                "TestPersonalMapCreation-ERROR-FailedToClickModalYes")

        try:
            wait = WebDriverWait(driver, params.long_wait)
            wait.until(EC.invisibility_of_element_located((By.ID, "modal-overlay")))
            wait.until(EC.element_to_be_clickable((By.ID, "left-controls")))
            sleep(3)
        except TimeoutException:
            helpers.print_timestamped_message(driver,
                                              "Map did not seem to reload after reset layout. "
                                              " Reset may be taking a very long time or the"
                                              " MODAL window may still be present")
            take_screenshot(driver, screenshots_dir,
                "TestPersonalMapCreation-ERROR-FailedToReloadMap")
            raise

        helpers.wait_until_batch_save_complete(driver)

        # grabbing the labels after an auto-arrange.
        after_arrange_labels = helpers.get_label_positions(driver)
        sleep(3)

        assert after_arrange_labels is not None, "No labels returned after the arrange"

        try:
            after_label = after_arrange_labels.pop()
            # printing out label positions.
            temp = "Auto arrange should result in new screen positions. " \
                   "Top offsets:  after-%s  before-%s" \
                   % (after_label['top'], before_label['top'])
            helpers.print_timestamped_message(driver, temp)
            # compare top offset positions of the first label.
            # these values should be different regardless of the label positions have changed.
            assert after_label['top'] != before_label['top'], \
                "Auto arrange did not work.  %s Label positions have not changed. %s" \
                % (after_label['top'], before_label['top'])

        except IndexError:
            take_screenshot(driver, screenshots_dir, "TestPersonalMapCreation-Before-JS-Script")
            helpers.print_timestamped_message(driver, str(after_arrange_labels))


        # give a little more time as the map layout frequently takes a varied amount of time
        sleep(10)

        driver.get(driver.current_url)

        sleep(1)

        try:
            modal_overlay = driver.find_element_by_id("modal-overlay")
            assert not modal_overlay.is_displayed()
        except:
            raise

        take_screenshot(driver, screenshots_dir,
                                "TestPersonalMapCreation-AfterResetMapAfterDone")
    except TimeoutException:
        take_screenshot(driver, screenshots_dir,
                                "TestPersonalMapCreation-ERROR-FailedToResetLayout")
        raise
    except UnexpectedAlertPresentException:
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-ERROR-UnexpectedAlertPresentException")
        alert = driver.switch_to_alert()
        alert.send_keys('8080')
        alert.dismiss()
        raise
    except:
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-ERROR-FailedToResetLayout")
        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# Does the map switcher list maps, and can I navigate with it?
# @pytest.mark.skipif(True, reason="Disabled for development")
def test_map_switcher(driver_load_personal_map_with_memory_stats, screenshots_dir):
    print(__name__, ':TestPersonalMapCreation.test_map_switcher()')

    driver = driver_load_personal_map_with_memory_stats

    try:

        wait = WebDriverWait(driver, params.wait_time)

        helpers.open_map_switcher(driver)

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#map-list')))

        take_screenshot(driver, screenshots_dir, "TestPersonalMapCreation-MapSwitcherLoaded")

        map_link = driver.find_element_by_partial_link_text('Top Artists')
        sleep(2)
        map_link.click()

        map.wait_global_ready(driver)

        take_screenshot(driver, screenshots_dir, "TestPersonalMapCreation-NavigatedToGlobalMap")

        helpers.open_map_switcher(driver)

        my_map_link = wait.until(EC.element_to_be_clickable((By.ID, 'my-map')))
        sleep(2)
        my_map_link.click()

        map.wait_personal_ready(driver)

        take_screenshot(driver, screenshots_dir, "TestPersonalMapCreation-NavigatedToPersonalMap")


    except:
        take_screenshot(
            driver, screenshots_dir, "TestUserPreferences-ERROR-FailedToNavigateViaMapSwitcher")
        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)


# @pytest.mark.skipif(True, reason="Disabled since add album is no longer valid, need to rewrite with artist pick.")
def test_clear_map(driver_load_personal_map_with_memory_stats, screenshots_dir):
    print(__name__, ':TestPersonalMapCreation.test_clear_map()')

    driver = driver_load_personal_map_with_memory_stats

    try:
        helpers.wait_until_batch_save_complete(driver)

        take_screenshot( driver, screenshots_dir,
             "TestPersonalMapCreation-BeforeClear")

        helpers.print_timestamped_message(driver, "Clearing")
        helpers.clear_personal_media_direct(driver)
        helpers.print_timestamped_message(driver, "Called clear")

        take_screenshot( driver, screenshots_dir,
             "TestPersonalMapCreation-Waiting for global map")

        map.wait_global_ready(driver)

        take_screenshot( driver, screenshots_dir,
             "TestPersonalMapCreation-ReturnedToGlobalMap")

        driver.execute_script("window.localStorage.clear();")

        driver.get(params.app_url + username)

        map.wait_personal_ready(driver)

        take_screenshot( driver, screenshots_dir,
             "TestPersonalMapCreation-PersonalMapAfterClear")

        artist_count = helpers.get_media_node_count(driver)

        assert artist_count == 0, "TestPersonalMapCreation-WrongArtistCount %s" % artist_count

    except TimeoutException:
        take_screenshot(
            driver, screenshots_dir, "TestPersonalMapCreation-ERROR-TimeoutError")
        raise
    except UnexpectedAlertPresentException:
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-ERROR-UnexpectedAlertPresentException")
        alert = driver.switch_to_alert()
        alert.send_keys('8080')
        alert.dismiss()
        #raise
    except:
        take_screenshot(driver, screenshots_dir,
            "TestPersonalMapCreation-ERROR-UncaughtException")
        raise
    finally:
        helpers.fail_if_modal(driver, screenshots_dir)

        driver.execute_script("window.localStorage.clear();")
        helpers.clear_personal_media_direct(driver, redirect=False)
        helpers.fast_sign_out(driver)
