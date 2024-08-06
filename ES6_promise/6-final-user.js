import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
    try {
        const userPromise = signUpUser(firstName, lastName);
        const photoPromise = uploadPhoto(fileName);

        await Promise.all([userPromise, photoPromise]);

        return [
            { status: 'fulfilled', value: await userPromise },
            { status: 'fulfilled', value: await photoPromise }
        ];
    } catch (error) {
        return [
            { status: 'rejected', value: error },
            { status: 'rejected', value: error }
        ];
    }
}

export default handleProfileSignup;
