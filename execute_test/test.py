from file_read_and_report.application import run_application


def test_app(file, top_n):
    expected_result = [['ahh!', 2], ['day', 2], ['everyone', 2], ['how', 2], ['was', 2],
                       ['Good', 1], ['Hi', 1], ['It', 1], ['Morning', 1], ['a', 1]]

    actual_result = run_application(file, top_n)
    if actual_result:
        assert (expected_result == actual_result), "Actual result {actual} " \
                                                "is different from expected " \
                                                "result {expected}".format(actual=actual_result,
                                                                           expected=expected_result)


if __name__ == "__main__":
    test_app('SampleTextData.txt', 10)
