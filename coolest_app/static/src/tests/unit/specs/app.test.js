import { mount, createLocalVue } from '@vue/test-utils';
// import Vuex from 'vuex';
import UserSettings from '@/vue/apps/UserSettings';

const localVue = createLocalVue();
// localVue.use(Vuex);

describe('UserSettings component', () => {
	/*
	let actions;
	let getters;
	let store;

	beforeEach(() => {
		actions = {
			requestJob: jest.fn(),
			newActivity: jest.fn(),
			deleteError: jest.fn(),
			deleteGTM: jest.fn(),
			newError: jest.fn(),
			newGTM: jest.fn(),
			editFluency: jest.fn(),
			editComment: jest.fn(),
			editReport: jest.fn(),
			reportJob: jest.fn(),
			submitJob: jest.fn(),
			submitBatch: jest.fn(),
		};
		getters = {
			getBatch: () => {
				return {
					tasks: [
						{
							id: '5a29910269e1e40018252c44',
							nr_words: 92,
							status: 'in_progress',
							time_taken: 10540,
						},
						{
							id: '5a29910269e1e40018252c45',
							nr_words: 92,
							status: 'in_progress',
							time_taken: 10540,
						},
					],
				};
			},
			getRegister: () => {
				return 'Informal';
			},
			getInstructions: () => {
				return {
					customer: 'These are instructions',
				};
			},
			getTask: () => {
				return {
					sourceContent: [
						{
							id: '0',
							text: 'olha aqui, um texto',
							annotations: [],
						},
					],
					targetContent: [
						{
							id: '0',
							text: 'look over here, a text',
							annotations: [],
						},
					],
				};
			},
			getErrorList: () => {
				return [];
			},
		};
		store = new Vuex.Store({
			state: {},
			actions,
			getters,
		});
	});
	*/
	test('Blank state', () => {
		const component = mount(UserSettings, {
			// store,
			localVue,
		});
		const main = component.find('.c-UserSettings').html();

		expect(main).toBeDefined();
	});
});
