import CheckboxGroupWithToggle from './CheckboxGroupWithToggle';
import phoneticSets from '../constants/phoneticSets';

export default function PhoneticGroups() {
    return (
        <div>
            {Object.keys(phoneticSets).map(groupName => (
                <CheckboxGroupWithToggle
                    groupName={groupName}
                    itemList={phoneticSets[groupName]}
                    idList={phoneticSets[groupName]}
                />
            ))}
        </div>
    )
}