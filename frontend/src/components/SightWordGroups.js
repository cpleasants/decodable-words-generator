import CheckboxGroupWithToggle from './CheckboxGroupWithToggle';
import sightWordSets from '../constants/sightWordsSets'

export default function PhoneticGroups() {
    return (
        <div>
            {Object.keys(sightWordSets).map(groupName => (
                <CheckboxGroupWithToggle
                    groupName={groupName}
                    itemList={sightWordSets[groupName]}
                />
            ))}
        </div>
    )
}