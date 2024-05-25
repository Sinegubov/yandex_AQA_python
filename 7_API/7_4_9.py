# мок вызвали хотя бы раз
mock_upload_photo.assert_called()

# мок вызвали только один раз
mock_upload_photo.assert_called_once()

# мок вызвали с аргументом 'photo.jpg'
mock_upload_photo.assert_any_call('photo.jpg')

# последний раз мок вызвали с аргументом 'photo.jpg'
mock_upload_photo.assert_called_with('photo.jpg')

# мок вызывался с аргументом 'photo.jpg' только один раз
mock_upload_photo.assert_called_once_with('photo.jpg')