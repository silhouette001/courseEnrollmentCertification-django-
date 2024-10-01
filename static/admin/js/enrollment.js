document.addEventListener('DOMContentLoaded', function() {
    const isCompletedField = document.getElementById('id_is_completed');
    const completionDateField = document.getElementById('id_completion_date').closest('.form-row');

    function toggleCompletionDate() {
        if (isCompletedField.checked) {
            completionDateField.style.display = '';
        } else {
            completionDateField.style.display = 'none';
        }
    }

    // Initially hide/show the field based on the current value
    toggleCompletionDate();

    // Add an event listener to toggle the field when the checkbox is clicked
    isCompletedCheckbox.addEventListener('change', toggleCompletionDate);
});
